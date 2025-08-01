from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    ingredients = request.form['ingredients']
    # For now, just pass ingredients back to the template
    return render_template('results.html', ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)