from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re

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
        self.user = None
    
    @classmethod
    def add_valid_recipe(cls, recipe_val):
        if not cls.is_valid(recipe_val):
            return False
        
        query = "INSERT INTO recipes (name, description, instructions, under, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under)s, %(user_id)s);"
        results = connectToMySQL(cls.DB).query_db(query, recipe_val)
        print("__ ADDED RECIPE __", results)
        return results
    
    @classmethod
    def get_recipes_by_id(cls, recipe_id):
        data = {"id" : recipe_id}
        query = """
        SELECT recipes.id, recipes.created_at, recipes.updated_at, instructions, description, name, date_made, under,
        users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
        FROM recipes
        JOIN users on users.id = recipes.user_id
        WHERE recipes.id = %(id)s
        """
        
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET RECIPE BY ID __", results)
        results = results[0]
        print("********** ___ GET BY ID RESULTS", results)
        recipe = cls(results)
        recipe.user = user.User(
                {
                    "id" : results["user_id"],
                    "first_name" : results['first_name'],
                    "last_name" : results['last_name'],
                    "last_name" : results['last_name'],
                    "email" : results['email'],
                    "created_at" : results['uc'],
                    "updated_at" : results['uu']
                }
            )
        return recipe
        
    @classmethod
    def delete_recipe(cls, id):
        data = {"id" : id}
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod 
    def update_recipe(cls, recipe_val, session_id):
        
        # authenticate user 
        recipe = cls.get_recipes_by_id(recipe_val['id'])
        if recipe.user.id != session_id:
            flash("You must be the creator to update this recipie")
            return False
        
        # validate input
        if not cls.is_valid(recipe_val):
            return False

        # update data to database
        query = "UPDATE recipies SET name=%(name)s, description=%(description)s, instructions=%(instructions)s,  date_made=%(date_made)s, under=%(under)s, created_at=NOW(), updated_at=NOW() WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, recipe_val)
        recipe = cls.get_recipes_by_id(recipe_val['id'])
        return recipe
    
    @classmethod
    def get_all_recipes(cls):
        # data = {"id" : id}
        query = """
        SELECT recipes.id, recipes.created_at, recipes.updated_at, instructions, description, name, date_made, under,
        users.id as user_id, first_name, last_name, email, users.created_at as uc, users.updated_at as uu
        FROM recipes
        JOIN users on users.id = recipes.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL RECIPIES __", results)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @staticmethod
    def is_valid(recipe_val):
        valid = True
        flash_string = "field is required and must be at least 3 characters"
        if len(recipe_val['name']) < 3:
            flash("Name " + flash_string)
            valid = False
        if len(recipe_val['description']) < 3:
            flash("Description ", flash_string)
            valid = False
        if len(recipe_val['instructions']) < 3:
            flash("Instructions ", flash_string)
        if len(recipe_val['date_made']) <= 0:
            flash("Date is required.")
            valid = False
        if "under" not in recipe_val:
            flash("Does your recipe take less than 30 minutes?")
            valid = False
        
        return valid