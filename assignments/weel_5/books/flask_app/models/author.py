from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB = "books_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
    
    @classmethod
    def get_all_author(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ ADDED FAVORITE __", results)
        return results
    
    @classmethod
    def unfavorited_authors(cls, data):
        query = """
        SELECT * FROM authors 
        WHERE authors.id 
        NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ UNFACORITED AUTHORS", results)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors
    
    @classmethod
    def get_by_id_authors_favorite_books(cls, data):
        query = """
        SELECT * FROM authors 
        LEFT JOIN favorites ON authors.id = favorites.author_id 
        LEFT JOIN books ON books.id = favorites.book_id 
        WHERE authors.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET BY ID AUTHORS FAVORITE BOOKS __", results)
        author = cls(results[0])
        # append all book objects to the instances favorite list
        for row in results:
            #if there are no favorites
            if row['books.id'] == None:
                break
            # common colum names come back with specified tables attached
            data = {
                "id" : row['books.id'],
                "title" : row['title'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
                
            }
            author.favorite_books.append(book.Book(data))
        return author