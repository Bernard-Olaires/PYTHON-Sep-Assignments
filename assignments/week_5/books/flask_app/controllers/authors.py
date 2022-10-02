from crypt import methods
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

@app.route('/author/<int:id>')
def show_author(id):
    data = {"id" : id}
    return render_template("show-author.html", author = Author.get_by_id_authors_favorite_books(data), unfavorited_books = Book.unfavorited_books(data))

@app.route('/join/book', methods=['POST'])
def join_book():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")

@app.route('/home')
def home():
    return redirect('/')

