from flask import Flask, render_template,request,redirect,url_for
from bson import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)


client = MongoClient("mongodb+srv://app1:fRH3SQCA9Tq5VG18@myfirstcluster-7pmlf.mongodb.net/Cookbook?retryWrites=true")
db = client.Cookbook
Recipes = db.Recipes

@app.route("/")
def home():
    pageRecipes = Recipes.find()
    return render_template("index.html",pageRecipes=pageRecipes)

@app.route("/viewRecipes")
def viewRecipes():
    return render_template("viewrecipes.html")

@app.route("/addRecipes")
def addRecipes():
    return render_template("addrecipes.html")

if __name__ == "__main__":
    app.run(debug=True)

