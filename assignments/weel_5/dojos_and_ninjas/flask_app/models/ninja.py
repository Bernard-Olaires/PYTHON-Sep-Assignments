from flask_app.config.mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection

# model the class after the ninjas table from our database
class Ninja:
    DB = "dojos_and_ninjas_schema"
    # setting db to be our database
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        # calling the connectToMySQL function with the schema we are targeting
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ GET ALL NINJAS __", results)
        ninjas = []
        #creating an empty list to append our instances of ninjas
        for ninja in results:
            ninjas.append( cls(ninja) )
        # Iterate over the db results and create instances of ninjas with cls
        return ninjas
    
    @classmethod
    def get_ninja_by_id(cls, id):
        data = {"id" : id}
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ GET NINJA BY ID __", results)
        return cls(results[0])
    
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ CREATE NINJA __", results)
        return results
    
    @classmethod
    def updated_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, created_at=NOW(), updated_at=NOW() WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("__ UPDATED NINJA __", results)
        return results
    
    @classmethod
    def delete_ninja(cls, id):
        data = {"id" : id}
        query = "DELETE FROM ninja WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("__ DELETED NINJA __", results)
        return results