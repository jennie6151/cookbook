from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/viewRecipes")
def viewRecipes():
    return render_template("viewrecipes.html")

@app.route("/addRecipes")
def addRecipes():
    return render_template("addrecipes.html")

if __name__ == "__main__":
    app.run(debug=True)