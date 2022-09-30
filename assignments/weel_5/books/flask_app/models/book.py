from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []
        
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL BOOKS __", results)
        books = []
        for book in results:
            books.append( cls(book) )
        return books
    
    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ CREATED BOOK __", results)
        return results
    
    @classmethod
    def get_by_id_books_favorited_by_author(cls, data):
        query = """
        SELECT * FROM books 
        LEFT JOIN favorites ON books.id = favorites.book_id 
        LEFT JOIN authors ON authors.id = favorites.author_id 
        WHERE books.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET BY ID BOOKS FAVORITED BY AUTHOR __", results)
        
        book = cls( results[0] )
        
        for row in results:
            if row['author.id'] == None:
                break
            data = {
                "id" : row['authors.id'],
                "name" : row['name'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            book.authors_who_favorited.append( author.Author(data))
        return book
    
    @classmethod
    def unfavorited_books(cls, data):
        query = """
        SELECT * FROM books 
        WHERE books.id 
        NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ UNFAVORITED BOOKS __", results)
        books = []
        for book in results:
            books.append( cls(book) )
        return books