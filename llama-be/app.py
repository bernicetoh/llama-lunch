from flask import Flask, request
app = Flask(__name__)
from flask_cors import CORS, cross_origin
from gradio_client import Client
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/', methods=['GET'])
def getLlama():
    # food_mapping = ['🍕 - Pizza', '🍔 - Hamburger', '🍟 - French Fries', '🍣 - Sushi', '🍦 - Ice Cream', '🍓 - Strawberry', '🍝 - Spaghetti', '🍜 - Steaming Bowl', '🍛 - Curry Rice', '🍤 - Shrimp', '🍩 - Doughnut', '🍪 - Cookie', '🍰 - Shortcake', '🍫 - Chocolate', '🍬 - Candy', '🍭 - Lollipop', '🍯 - Honey', '🍍 - Pineapple', '🥑 - Avocado', '🥖 - Baguette', '🧀 - Cheese', '🍇 - Grapes', '🍈 - Melon', '🍉 - Watermelon', '🍊 - Tangerine', '🍋 - Lemon', '🍌 - Banana', '🍎 - Apple', '🍐 - Pear', '🍑 - Peach', '🍒 - Cherries', '🥕 - Carrot', '🥦 - Broccoli', '🍄 - Mushroom', '🍅 - Tomato', '🥔 - Potato', '🥓 - Bacon', '🥞 - Pancakes', '🍽️ - Plated Fork and Knife', '🥢 - Chopsticks', '🌮 - Taco', '🌯 - Burrito', '🍖 - Meat', '🥩 - Steak', '🍗 - Chicken Leg', '🍲 - Pot of Food', '🥗 - Green Salad', '🍠 - Roasted Sweet Potato', '🍢 - Oden', '🍥 - Fish Cake with Swirl', '🍡 - Dango', '🍧 - Shaved Ice', '🍨 - Ice Cream', '🎂 - Cake', '🧁 - Cupcake', '🥧 - Pie', '🥭 - Mango', '🍆 - Eggplant', '🥒 - Cucumber', '🌽 - Corn', '🥜 - Peanuts', '🌰 - Chestnut', '🍞 - Bread', '🥐 - Croissant', '🧇 - Waffle', '🌭 - Hot Dog', '🥪 - Sandwich', '🥟 - Dumpling', '🥨 - Pretzel', '🥯 - Bagel', '🍴 - Fork and Knife', '🥄 - Spoon']
    food_mapping = ['🍕 - Pizza', '🍔 - Hamburger', '🍟 - Fries', '🍣 - Sushi', '🍦 - Ice Cream', '🍓 - Strawberry', '🍝 - Spaghetti', '🍛 - Curry Rice', '🍤 - Shrimp', '🍩 - Doughnut', '🍪 - Cookie', '🍫 - Chocolate', '🍬 - Candy', '🍯 - Honey', '🍍 - Pineapple', '🥑 - Avocado', '🥖 - Baguette', '🧀 - Cheese', '🍇 - Grapes', '🍉 - Watermelon', '🍊 - Tangerine', '🍋 - Lemon', '🍌 - Banana', '🍎 - Apple', '🍐 - Pear', '🍑 - Peach', '🍒 - Cherries', '🥕 - Carrot', '🥦 - Broccoli', '🍄 - Mushroom', '🍅 - Tomato', '🥔 - Potato', '🥓 - Bacon', '🥞 - Pancakes', '🍽️ - Plate', '🥢 - Chopsticks', '🌮 - Taco', '🌯 - Burrito', '🍖 - Meat', '🥩 - Steak', '🍗 - Chicken', '🦪 - Oyster', '🍲 - Pot of Food', '🥗 - Salad', '🎂 - Cake', '🧁 - Cupcake', '🥧 - Pie', '🥭 - Mango', '🍆 - Eggplant', '🥒 - Cucumber', '🌽 - Corn', '🥜 - Peanuts', '🌰 - Chestnut', '🍞 - Bread', '🥐 - Croissant', '🧇 - Waffle', '🌭 - Sausage', '🥪 - Sandwich', '🥟 - Dumpling', '🥨 - Pretzel', '🥯 - Bagel', '🍴 - Fork and Knife', '🧂 - Salt']

    prompt = request.args.get('prompt')
    system_prompt = \
        "You are a chef brainstorming recipes to cook with the given ingredients. You must give me a recipe that uses only the ingredients input by the user. Your answers should not include ingredients not specified by the user. Come up with a succinct name for the recipe. Bold appropriate headings such as Ingredients and Duration using markdown.\n" + \
        "Here is the list of emojis mapping: " + str(food_mapping) + "\n\n" + \
        "EXAMPLE 1:\n" + \
        "Ingredients - eggs, bread, butter, bacon, Hollandaise Sauce\n" + \
        "Recipe -\n" + \
        "Title: Eggs Benedict\n" + \
        "Duration: 30minutes\n" + \
        "Ingredients:\n" + \
        "+ 4 eggs 🥚\n" + \
        "+ 2 slices of bread 🍞\n" + \
        "+ 1 tablespoon of butter 🧈\n" + \
        "+ 2 slices of bacon 🥓\n" + \
        "+ 1/2 cup of Hollandaise Sauce\n" + \
        "Steps:\n" + \
        "1. Poach 2 eggs in simmering water for 3-5 minutes or until whites are set and yolks are cooked to desired doneness.\n" + \
        "2. Make hollandaise sauce with 2 other eggs, by separating egg white and yolk, mix with butter\nSeparate egg white and yolk, then mix with melted butter in a heatproof bowl. Whisk until smooth and creamy.\n" + \
        "3. Fry bacon in a large skillet over medium heat until crispy and golden brown. Drain on paper towels.\n" + \
        "4. Toast bread with bacon oil using the same skillet used for frying bacon. Brush with melted bacon fat for added flavor.\n" + \
        "5. Arrange the poached eggs on the toasted bread. Gently pour the hollandaise sauce over the eggs. Add the crispy bacon slices to the side. Serve immediately, garnished with a sprinkle of fresh herbs if desired 😋" + \
        "\n\n" + \
        "EXAMPLE 2:\n" + \
        "Ingredients - pasta, thyme, butter, garlic, ham, sausage\n" + \
        "Recipe -\n" + \
        "Title: Thyme and Herb Pasta\n" + \
        "Duration: 25 minutes\n" + \
        "Ingredients:\n" + \
        "+ 8 oz pasta of your choice 🍝\n" + \
        "+ 1 tablespoon of butter 🧈\n" + \
        "+ 2 cloves of garlic, minced 🧄\n" + \
        "+ 1/4 cup of chopped ham 🥩\n" + \
        "+ 1/4 cup of chopped sausage\n" + \
        "+ Fresh thyme, chopped (optional) 🌿\n" + \
        "Steps:\n" + \
        "1. Cook pasta according to package instructions until al dente 👌. Drain and set aside.\n" + \
        "2. In a large skillet, melt 1 tablespoon of butter over medium heat. Add 2 cloves of minced garlic and sauté for 1-2 minutes until fragrant.\n" + \
        "3. Add 1/4 cup of chopped ham and 1/4 cup of chopped sausage to the skillet. Cook for 2-3 minutes until the meat is lightly browned.\n" + \
        "4. Add the cooked pasta to the skillet and toss with the meat and garlic mixture until well combined.\n" + \
        "5. Season with fresh thyme (if using) and serve hot 🤤\n" + \
        "Enjoy your delicious and easy Thyme and Herb Pasta!" + \
        "\n\n" + \
        "Generate Recipe\n" + \
        "Ingredients - "

    client = Client("https://huggingface-projects-llama-2-7b-chat.hf.space/--replicas/gm5p8/") # 7B
    # client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/fx2sq/") # 70B
    result = client.predict(
        prompt, # str  in 'parameter_7' Textbox component 
        system_prompt,
        # 7b
        1984,	# int | float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
		0.75,	# int | float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
		0.8,	# int | float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
		125,  # int | float (numeric value between 1 and 1000) in 'Top-k' Slider component
		1,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
        # 70b
        # 0.45, # temperature
        # 4096, # max_new_tokens
        # 0.8, # top_p
        # 1.1, # repetition
        api_name="/chat"
    )
    print(result)
    return result
