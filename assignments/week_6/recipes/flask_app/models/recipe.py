from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User

class Recipe:
    DB = "recipes"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
    
    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT * FROM recipes 
        LEFT JOIN users on users.id = recipes.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL RECIPES __", results)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id":row['users.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "email":row['email'],
                "password":row['password'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at']
            }
            creator = User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def get_recipe(cls, recipe_id):
        data = {"id" : recipe_id}
        query = """
        SELECT * FROM recipes 
        LEFT JOIN users on users.id = recipes.user_id WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        result = result[0]
        recipe = cls(result)
        recipe.creator = User(
                {
                    "id":result['users.id'],
                    "first_name":result['first_name'],
                    "last_name":result['last_name'],
                    "email":result['email'],
                    "password":result['password'],
                    "created_at":result['created_at'],
                    "updated_at":result['updated_at']
                }
            )
        return recipe
    
    @classmethod
    def create_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, date_made, under, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s, %(user_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update_recipe(cls,data):
        query = """
        UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under=%(under)s, date_made=%(date_made)s, user_id=%(user_id)s WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        print("__ UPDATE RECIPE __", result)
        return result
    
    
    @classmethod
    def delete_recipe(cls,recipe_id):
        data = {"id":recipe_id}
        query = """
        DELETE FROM recipes WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instuctions")
            is_valid = False
        if len(recipe['date_made']) < 3:
            flash("Date")
            is_valid = False
        if "under" not in recipe:
            flash("Is the recipe under 30 Minutes?")
            is_valid = False
        return is_valid