from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojo()
    return render_template("index.html", all_dojos = dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    dojos_with_ninjas = Dojo.get_dojo_with_ninja(id)
    return render_template("dojo.html", dojo = dojos_with_ninjas)


@app.route('/home')
def home():
    return redirect('/')