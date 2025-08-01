from flask import Flask, render_template, request
import requests
import os

load_dotenv()  #loading environment variables from .env file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recipes = []
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        #PLaceholder for API call
        recipes = get_recipes(ingredients)
    return render_template('index.html', recipes=recipes)

def get_recipes(ingredients):
    api_key = os.environ.get('SPOONACULAR_API_KEY')
    if not api_key:
        return []

    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'ingredients': ingredients,
        'number': 5,
        'apiKey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    recipes = [{'title': item['title']} for item in data]

    return recipes



if __name__ == '__main__':
    app.run(debug=True)