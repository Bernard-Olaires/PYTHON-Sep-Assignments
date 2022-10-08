from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    all_recipes = Recipe.get_all_recipes()
    return render_template("dashboard.html", logged_in_user = logged_in_user, recipes = all_recipes)

@app.route('/view/recipe/<int:id>')
def view_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    recipe_to_show = Recipe.get_recipe(id)
    return render_template("recipe-details.html", logged_in_user = logged_in_user, recipe = recipe_to_show)

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    if Recipe.validate_recipe(request.form):
        Recipe.create_recipe(request.form)
        return redirect("/dashboard")
    return redirect('/add/recipe')

@app.route('/add/recipe')
def add_recipe():
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    return render_template("add-recipe.html", logged_in_user = logged_in_user)

@app.route("/edit/recipe/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user_by_id(session["user_id"])
    recipe_to_edit= Recipe.get_recipe(id)
    return render_template("edit-recipe.html",logged_in_user=logged_in_user, recipe = recipe_to_edit)

@app.route('/update/recipe/<int:id>', methods=['POST'])
def update_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    if Recipe.validate_recipe(request.form):
        Recipe.update_recipe(request.form)
        return redirect("/dashboard")
    return redirect(f"/edit/recipe/{id}")

@app.route("/delete/recipe/<int:id>")
def delete_book(id):
    if "user_id" not in session:
        return redirect("/")
    Recipe.delete_recipe(id)
    return redirect('/dashboard')