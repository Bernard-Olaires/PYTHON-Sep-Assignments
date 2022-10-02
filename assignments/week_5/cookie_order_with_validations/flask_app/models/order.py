# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# model the class after the user table from our database

class Order:
    DB = "cookie_orders"
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL ORDERS __", results)
        orders = []
        for order in results:
            orders.append( cls(order) )
        return orders
    
    @classmethod
    def get_order_by_id(cls, id):
        data = {"id" : id}
        query = "SELECT * FROM orders WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET ORDER BY ID__ ", results)
        return cls(results[0])
    
    @classmethod
    def new_order(cls, data):
        query = "INSERT INTO orders (name, cookie_type, num_of_boxes) VALUES  (%(name)s, %(cookie_type)s, %(num_of_boxes)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ NEW ORDER __", results)
        return results
    
    @classmethod
    def update_order(cls, data):
        query = "UPDATE orders SET name=%(name)s, cookie_type=%(cookie_type)s, num_of_boxes=%(num_of_boxes)s WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ UPDATED USER __", results)
        return results
    
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) <= 0:
            flash("First Name is required")
            is_valid = False
        if len(order['cookie_type']) <= 0:
            flash("Last Name is required")
        if len(order['num_of_boxes']) <= 0:
            flash("Number of boxes required.")
        return is_valid