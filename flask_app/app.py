from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)


client = MongoClient(
    "mongodb+srv://app1:fRH3SQCA9Tq5VG18@myfirstcluster-7pmlf.mongodb.net/Cookbook?retryWrites=true")
db = client.Cookbook
Recipes = db.Recipes


@app.route("/")
def home():
    pageRecipes = Recipes.find()
    return render_template("index.html", pageRecipes=pageRecipes)

@app.route("/search", methods=['GET'])  
def search():   
    recipeSearch=request.values.get("recipeSearch")  
    refer="recipeTitle"
    if(recipeSearch=="_id"):  
        recipe = Recipes.find({refer:ObjectId(recipeSearch)})  
    else:  
        recipe = Recipes.find({refer:recipeSearch})  
    return render_template('searchresults.html',searchResults=recipe)  

@app.route("/viewRecipes")
def viewRecipes():
    id=request.values.get("_id")  
    recipe=Recipes.find({"_id":ObjectId(id)}) 
    return render_template("viewrecipes.html", recipe=recipe)


@app.route("/addRecipes")
def addRecipes():
    return render_template("addrecipes.html")

@app.route("/edit")  
def edit ():  
    id=request.values.get("_id")  
    recipe=Recipes.find({"_id":ObjectId(id)})  
    return render_template('editrecipes.html', recipe=recipe)

@app.route("/updateRecipe", methods=['POST'])  
def updateRecipe ():
    id=request.values.get("_id") 
    username = request.values.get("username")
    recipeTitle = request.values.get("recipeTitle")
    recipeIngredients = request.values.get("recipeIngredients")
    recipeMethod = request.values.get("recipeMethod")
    prepTime = request.values.get("prepTime")
    cookTime = request.values.get("cookTime")
    recipeServes = request.values.get("recipeServes")
    recipeNotes = request.values.get("recipeNotes")
    Recipes.update({"_id":ObjectId(id)}, {'$set':{"username":username, "recipeTitle":recipeTitle, "recipeIngredients":recipeIngredients,
                    "recipeMethod":recipeMethod, "prepTime":prepTime, "cookTime":cookTime, "recipeServes":recipeServes, "recipeNotes":recipeNotes}})
    return redirect("/")

@app.route("/remove")  
def remove ():  
    id=request.values.get("_id")  
    Recipes.remove({"_id":ObjectId(id)})  
    return redirect("/")

@app.route("/action", methods=['POST'])
def action():
    username = request.values.get("username")
    recipeTitle = request.values.get("recipeTitle")
    recipeIngredients = request.values.get("recipeIngredients")
    recipeMethod = request.values.get("recipeMethod")
    prepTime = request.values.get("prepTime")
    cookTime = request.values.get("cookTime")
    recipeServes = request.values.get("recipeServes")
    recipeNotes = request.values.get("recipeNotes")
    Recipes.insert({"username": username, "recipeTitle": recipeTitle, "recipeIngredients": recipeIngredients,
                    "recipeMethod": recipeMethod, "prepTime": prepTime, "cookTime": cookTime, "recipeServes": recipeServes, "recipeNotes": recipeNotes})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
