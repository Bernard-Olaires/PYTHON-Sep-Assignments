from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def add_ninja():
    dojos = Dojo.get_all_dojo()
    return render_template("ninja.html", all_dojos = dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print("A")
    print(request.form)
    Ninja.create_ninja(request.form)
    return redirect('/')

@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    return render_template("edit.html", ninja = Ninja.get_ninja_by_id(id))

@app.route('/ninja/update', methods=['POST'])
def update_ninja():
    print(request.form)
    Ninja.updated_ninja(request.form)
    return redirect("/dojos")

@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    Ninja.delete_ninja(id)
    return redirect('/')
