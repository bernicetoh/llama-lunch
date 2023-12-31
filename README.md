# LlaMa Lunch

<p align="center">
  <img src="llama-fe/src/assets/cook.png" alt="logo" width="300px">
</p>

Integrated with Meta's Large Language Model, [LlaMa2](https://ai.meta.com/llama/), LlaMa Lunch is an interactive AI-cook assistant designed to inspire you with recipe ideas for your upcoming culinary endeavours.

Just input the ingredients you wish to work with, and let LlaMa Lunch seamlessly generate a customized recipe tailored to your preferences!

In the interest of convenience, LlaMaLunch leverages the API endpoint provided by [Hugging Face](https://huggingface.co/spaces/huggingface-projects/llama-2-7b-chat) rather than relying on the training code located in the [`train_code/`](./train_code/) directory. But the behaviour is replicated as shown in the Jupyter Notebook.

We have detailed our efforts and attempts in [`train_code/`](./train_code/).

## Product Demo
All the user needs to do is input some ingredients and LlaMaLunch will generate a recipe using only the ingredients provided as shown below:

![demo](./train_code/in_context_with_llama/demo.png)

## Getting Started

### Run the backend server

1. In the project directory, `cd llama-be`
2. Run `FLASK_APP=app.py flask run` to start the backend server on localhost.

### Run the frontend server

1. In the project directory, `cd llama-fe`
2. Run `npm run start` to start the server.
3. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Model Parameters

The LlaMa2 model from Huggingface accepts 7 parameters: `Message`, `System prompt`, `Max new tokens`, `Temperature`, `Top-p (nucleus sampling)`, `Top-k`, and `Repitition penality`.

- **`Message`**: The user's input prompt

- **`System prompt`**: A block of text appended before the `Message` to steer LlaMa2's responses. This helps to guide the model's subsequent behaviour through preemptive framing of the discussion paramters.

  In the context of LlaMa Lunch, we want to generate chef-like recipes that are feasible. As such, we include a system prompt of 'You are a chef brainstorming recipes'. This directive ensures that the generated recipes are not just creative but also within the realm of feasibility.

The decision to incorporate a persona (Chef) into the model was influenced by the insights from the [LlaMa2 paper](https://arxiv.org/pdf/2307.09288.pdf) that details the type of prompts the model can handle:

  <p align="center">
    <img src="llama-fe/src/assets/llama-prompt.png" alt="llama prompts" width="600px">
  </p>

- **`Max new tokens`**: Maximum number of tokens to generate.
  This determines the maximum length of the model's output. Setting a lower value limits the maximum number of tokens generated to avoid excessively long responses.

  To generate more elaborate and extended recipes, we have configured this value to its maximum setting.

- **`Temperature`**: Determines the randomness of the outputs.
  A higher temperature value generates a vastly different output. A low temperature value generates a more consistent and conservative responses.

  For LlaMa Lunch, our goal is to produce captivating recipes, so we opted for a higher temperature setting to enhance the diversity and creativity of our generated output.

- **`Repetition penalty`**: Penalizes or reduces the probability of generating tokens that have recently appeared in the generated text. A value greater than 1 discourages word repetition in the model's output.

  Similar to the rationale behind the value set for `Temperature`, we want to ensure creativity in recipes generated. Hence, this means reducing repetition by increasing the repetition penalty value.

- **`Top-p`**: Constraints the next token selection to the top-k most likely tokens at each step.

- **`Top-k`**: Limits the selection of tokens to a subset of the vocabulary with cumulative probability mass up to a threshold value. This helps in controlling the diversity of generated output.
