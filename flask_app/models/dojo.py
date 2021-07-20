from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app.models.ninja import Ninja

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all_dojos(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for item in results:
            # new_dojo = Dojo(item) << If you want to clarify (cls(item)) below.
            dojos.append(cls(item))
            # I did it the other way in the get_all_dojos_with_ninjas @classmethod below
        return dojos

    @classmethod
    def show_one_dojo(cls, data):

        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id ORDER BY dojos.id;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return Dojo(results[0])

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (location) VALUES (%(dojo_location)s);"

        new_dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return new_dojo