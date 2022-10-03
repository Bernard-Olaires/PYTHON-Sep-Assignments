from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Recipe:
    DB = "recipes"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL RECIPIES __", results)
        recipes = []
        for recipe in results:
            recipes.append(cls (recipe) )
        return recipes
    
    @classmethod
    def get_recipes_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET RECIPES BY ID __", results)
        return cls(results[0])
    
    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under)s, %(user_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ ADDED RECIPE __", results)
        return results
    
    @classmethod 
    def update_recipe(cls, data):
        query = "UPDATE recipies SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under=%(under)s, created_at=NOW(), updated_at=NOW() WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def delete_recipe(cls, id):
        data = {"id" : id}
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results