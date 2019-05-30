from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://app1:fRH3SQCA9Tq5VG18@myfirstcluster-7pmlf.mongodb.net/Cookbook?retryWrites=true"
mongo = PyMongo(app)

Recipes = mongo.db.Recipes

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

@app.route("/createRecipe", methods=['POST'])
def action():
    username = request.values.get("username")
    recipeTitle = request.values.get("recipeTitle")
    if "recipeImage" in request.files:
        recipeImage = request.files["recipeImage"]
        mongo.save_file(recipeImage.filename, recipeImage)
    recipeIngredients = request.values.get("recipeIngredients")
    recipeMethod = request.values.get("recipeMethod")
    prepTime = request.values.get("prepTime")
    cookTime = request.values.get("cookTime")
    recipeDifficulty = request.form.get("recipeDifficulty")
    recipeServes = request.values.get("recipeServes")
    dietType = request.form.getlist("dietType")
    cuisineType = request.form.get("cuisineType")
    recipeNotes = request.values.get("recipeNotes")
    Recipes.insert({"username": username, "recipeTitle": recipeTitle, "recipeImage": recipeImage.filename, "recipeIngredients": recipeIngredients,
                    "recipeMethod": recipeMethod, "prepTime": prepTime, "cookTime": cookTime, "recipeDifficulty": recipeDifficulty, "recipeServes": recipeServes, "dietType": dietType, "cuisineType": cuisineType, "recipeNotes": recipeNotes})
    return redirect("/")

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
    recipeDifficulty = request.form.get("recipeDifficulty")
    recipeServes = request.values.get("recipeServes")
    dietType = request.form.getlist("dietType")
    cuisineType = request.form.get("cuisineType")
    recipeNotes = request.values.get("recipeNotes")
    Recipes.update({"_id":ObjectId(id)}, {'$set':{"username":username, "recipeTitle":recipeTitle, "recipeIngredients":recipeIngredients,
                    "recipeMethod":recipeMethod, "prepTime":prepTime, "cookTime":cookTime, "recipeDifficulty": recipeDifficulty, "recipeServes": recipeServes, "dietType": dietType, "cuisineType": cuisineType, "recipeNotes":recipeNotes}})
    return redirect("/")

@app.route("/remove")  
def remove ():  
    id=request.values.get("_id")  
    Recipes.remove({"_id":ObjectId(id)})  
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
