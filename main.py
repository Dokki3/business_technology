from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


if __name__ == '__main__':
    app.run(debug=True)

