from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all_author()
    return render_template("index.html", all_authors = authors)

@app.route('/create/author', methods=['POST'])
def create_author():
    print(request.form)
    Author.create_author(request.form)
    return redirect('/authors')