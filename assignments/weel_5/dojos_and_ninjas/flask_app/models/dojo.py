from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    
    
    #     SELECT * FROM dojos
    # LEFT JOIN ninjas on ninjas.dojo_id = dojos.id
    # WHERE dojos.id = %(id)s;