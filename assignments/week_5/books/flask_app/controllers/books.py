from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def add_book():
    return render_template("books.html", all_books = Book.get_all_books())

@app.route('/create/book', methods=['POST'])
def create_book():
    print(request.form)
    Book.create_book(request.form)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data = {"id" : id}
    unfavorited_authors = Author.unfavorited_authors(data)
    
    return render_template("show-book.html", book= Book.get_by_id_books_favorited_by_author(data) , author = unfavorited_authors)

@app.route('/join/author', methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")