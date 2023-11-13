import transformers
import fire
import torch

from datasets import load_dataset
from torch import cuda
from peft import (
    LoraConfig,
    get_peft_model,
    get_peft_model_state_dict,
    prepare_model_for_int8_training,
    set_peft_model_state_dict,
    PrefixTuningConfig,
    TaskType
)
from transformers import LlamaForCausalLM, LlamaTokenizer

from typing import List

from huggingface_hub import login



def train(
    # model/data params
    base_model: str = "meta-llama/Llama-2-7b-chat-hf",
    data_path: str = "m3hrdadfi/recipe_nlg_lite",
    output_dir: str = "./output",

    micro_batch_size: int = 4,
    gradient_accumulation_steps: int = 4,
    num_epochs: int = 3,
    learning_rate: float = 3e-4,
    val_set_size: int = 2000,

    # lora hyperparams
    lora_r: int = 8,
    lora_alpha: int = 16,
    lora_dropout: float = 0.05,
    lora_target_modules: List[str] = [
        "q_proj",
        "v_proj",
    ]
):

    device_map = "auto"

    #login to hugging face
    access_token_read ="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"
    login(token = access_token_read)


    # Step 1: Load the model and tokenizer

    model = LlamaForCausalLM.from_pretrained(
        base_model,
        # load_in_8bit=True, # Add this for using int8
        torch_dtype=torch.float16,
        device_map=device_map,
    )

    tokenizer = LlamaTokenizer.from_pretrained(base_model)
    tokenizer.pad_token_id = 0

    #Add this for training LoRA

    config = LoraConfig(
        r=lora_r,
        lora_alpha=lora_alpha,
        target_modules=lora_target_modules,
        lora_dropout=lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
    )

    model = get_peft_model(model, config)

    model = prepare_model_for_int8_training(model) # Add this for using int8


    # Step 2: Load the data

    if data_path.endswith(".json") or data_path.endswith(".jsonl"):
        data = load_dataset("json", data_files=data_path)
    else:
        data = load_dataset(data_path)

    # Step 3: Tokenize the data

    def tokenize(data):
        source_ids = tokenizer.encode(data['ingredients'])
        target_ids = tokenizer.encode(data['steps'])

        input_ids = source_ids + target_ids + [tokenizer.eos_token_id]
        labels = [-100] * len(source_ids) + target_ids + [tokenizer.eos_token_id]

        return {
            "input_ids": input_ids,
            "labels": labels
        }

    #split the data to train/val set
    train_val = data["train"].train_test_split(
        test_size=val_set_size, shuffle=False, seed=42
    )
    train_data = (
        train_val["train"].shuffle().map(tokenize)
    )
    val_data = (
        train_val["test"].shuffle().map(tokenize)

    )

    # Step 4: Initiate the trainer

    trainer = transformers.Trainer(
        model=model,
        train_dataset=train_data,
        eval_dataset=val_data,
        args=transformers.TrainingArguments(
            per_device_train_batch_size=micro_batch_size,
            gradient_accumulation_steps=gradient_accumulation_steps,
            warmup_steps=100,
            num_train_epochs=num_epochs,
            learning_rate=learning_rate,
            fp16=True,
            logging_steps=10,
            optim="adamw_torch",
            evaluation_strategy="steps",
            save_strategy="steps",
            eval_steps=200,
            save_steps=200,
            output_dir=output_dir,
            save_total_limit=3
        ),
        data_collator=transformers.DataCollatorForSeq2Seq(
            tokenizer, pad_to_multiple_of=8, return_tensors="pt", padding=True
        ),
    )

    trainer.train()


    # Step 5: save the model
    model.save_pretrained(output_dir)


if __name__ == "__main__":
    fire.Fire(train)