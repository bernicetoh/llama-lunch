from flask import Flask, request
app = Flask(__name__)
from flask_cors import CORS, cross_origin
from gradio_client import Client
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/', methods=['GET'])
def getLlama():
    prompt = request.args.get('prompt')
    client = Client("https://huggingface-projects-llama-2-7b-chat.hf.space/--replicas/gm5p8/")
    result = client.predict(
        prompt, # str  in 'parameter_7' Textbox component 
        "You are a chef brainstorming recipes to cook. Always include emojis and bold appropriate headings such as 'Title' and 'Ingredients', give me a recipe that uses only the ingredients input by the user. Your answers should not include ingredients not mentioned by the user. It does not always have to be Eggs Benedict. Come up with a title for the dish.\n" + \
        "An example of a recipe:\n" + \
        "Recipe: Eggs Benedict 🍳\n" + \
        "----------------------\n" + \
        "Ingredients:\n" + \
        "🥚 2 eggs\n" + \
        "🍞 2 slices of bread\n" + \
        " 🧈 1 tablespoon of butter\n" + \
        "🥭 1/2 cup of Hollandaise Sauce\n\n" + \
        "🕙 Duration: 30 min\n\n" + \
        "Steps:\n" + \
        "1. Poach egg\n Poach egg in simmering water for 3-5 minutes or until whites are set and yolks are cooked to desired doneness.\n" + \
        "2. Make hollandaise sauce by separating egg white and yolk, mix with butter\nSeparate egg white and yolk, then mix with melted butter in a heatproof bowl. Whisk until smooth and creamy.\n" + \
        "3. Fry Bacon\nFry bacon in a large skillet over medium heat until crispy and golden brown. Drain on paper towels.\n" + \
        "4. Toast bread with bacon oil\n Toast bread in the same skillet used for frying bacon. Brush with melted bacon fat for added flavor.\n" + \
        "5. Plate and serve beautifully.\n",
            2048,	# int | float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
		0.72,	# int | float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
		0.73,	# int | float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
		0,	# int | float (numeric value between 1 and 1000) in 'Top-k' Slider component
		1.1,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat"
    )
    print(result)
    return result
