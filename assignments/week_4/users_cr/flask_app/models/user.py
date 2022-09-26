# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database

class User:
    DB = "users_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# no we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ ALL FRIENDS __", results)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_user_by_id(cls, id):
        data = {"id":id}
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ GET ONE PRODUCT __", results)
        return cls(results[0])
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ INSERT ___", results)
        return results
    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s,created_at=NOW(),updated_at=NOW() WHERE id= %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ UPDATED USER __", results)
        return results
    
    @classmethod
    def delete_user(cls, id):
        data = {"id":id}
        query = "DELETE FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ DELETE USER ___", results)
        return results
    