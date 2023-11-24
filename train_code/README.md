# Fine-Tuning & Re-training

This folder details our attempts and efforts in tailoring LLaMa2 model. The prompt used in our back-end was experimented and dervied from our efforts here.

## Fine-tuning
We first attempted prompt engineering and experimented with carefully curated prompts. The code is in [`in_context_with_llama/`](./in_context_with_llama/) folder. We realised the choice of words and the structure of the prompt can drastically influence the output of the model. This aligns with what we have learnt, and a well-engineered prompt can essentially be thought of as placing more 'attention' (relevance) to certain inputs, thereby generating related outputs. Our engineered prompt (the one used in our back-end) is used in our final [`engine.ipynb`](./in_context_with_llama/engine.ipynb). Poor prompting may generate undesirable (or too generic) output as shown in our [`poor prompting`](./in_context_with_llama/poor_prompt_example.ipynb) example.

## LoRA
Prompt engineering actually worked surprisingly well. When showed to a couple of friends who frequently cook, they were genuinely impressed by the details and precision generated in the recipes. While the performance is already very much satisfactory, we tried experimenting further by re-training the model with LoRA layers. Unfortunately, after numerous attempts, even with Google Collab Pro, we simply do not have sufficient memory to completely train the model. Still, the code is provided in our train code, [`Promptly_plated_LORA.ipynb`](./lora_train/Promptly_plated_LORA.ipynb) but it shows a cuda memory constraint error.

Dataset used in re-training the model is obtained from [`Hugging Face`](https://huggingface.co/datasets/recipe_nlg).

## Legacy
All out other misc attempts and old code / model / engine is stored here.