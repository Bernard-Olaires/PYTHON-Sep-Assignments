from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import flash

@app.route('/recipe/home')
def recipe_home():
    if "user_id" not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect('/')
    
    user = User.get_user_by_id(session['user_id'])
    all_recipes = Recipe.get_all_recipes()
    
    return render_template("dashboard.html", user = user, recipes = all_recipes)

@app.route('/view/recipe/<int:id>')
def view_recipe(id):
    user = User.get_user_by_id(session['user_id'])
    all_recipes = Recipe.get_recipes_by_id(id)
    return render_template("view-recipe.html", user=user, recipe = all_recipes)