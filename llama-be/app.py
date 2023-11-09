from flask import Flask, request
app = Flask(__name__)
from flask_cors import CORS, cross_origin
from gradio_client import Client
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/', methods=['GET'])
def getLlama():
    prompt = request.args.get('prompt')
    client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/")
    result = client.predict(
            prompt, # str  in 'parameter_7' Textbox component 
            "Include emojis and decorate your answer, Give me a formatted (in a table format like markdown table) recipe that uses only the ingredients input by the user. Make sure no extra ingredients are used. Display in a table format to beautify it. If the user provides Eggs, only Eggs should appear under ingredients. Please bold appropriate words. For example, user provides: Eggs, Bread, Butter, Hollandaise Sauce.\n" + \
            "The recipe you provide is:\n" + \
            "Title: Eggs Benedict\n" + \
            "Ingredients: Eggs, Bread, Butter, Hollandaise Sauce\n" + \
            "Duration: 30 min\n" + \
            "Steps:\n" + \
            "1. Poach egg\n" + \
            "2. Make hollandaise sauce by separating egg white and yolk, mix with butter\n" + \
            "3. Fry Bacon\n" + \
            "4. Toast bread with bacon oil\n" + \
            "5. Plate and serve beautifully\n",
            1,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component, 'randomness' of outputs, 0.0 is the min and 1.0 the max
            4096,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
            0.1,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
            1,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component, without this output begins repeating
            api_name="/chat"
    )
    print(result)
    return result
