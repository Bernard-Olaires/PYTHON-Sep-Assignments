# the controller will run our @app.routes and the function within them
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User #--- UN COMMENT ME ----


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("users.html", all_users=users)

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.create_user(request.form)
    return redirect('/users')

@app.route('/user/edit/<id>')
def edit_user(id):
    return render_template("edit_user.html", user=User.get_user_by_id(id))

@app.route('/user/update', methods=['POST'])
def update():
    print(request.form)
    User.update_user(request.form)
    return redirect("/users")

@app.route("/users/show/<int:id>")
def show_user(id):
    one_user = User.get_user_by_id(id)
    return render_template("show.html", user=one_user)
    
@app.route("/users/<id>/delete")
def delete_user(id):
    User.delete_user(id)
    return redirect('/')

