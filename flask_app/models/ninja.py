from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"

        new_ninja_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return new_ninja_id


    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        return results

    # @classmethod
    # def get_one_dojo_with_ninjas(cls, data):
        
    #     query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id ORDER BY dojos.id;"

    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    #     dojos = []

    #     for item in results:
    #         if len(dojos) == 0:
    #             new_dojo = Dojo(item)
    #             dojos.append(new_dojo)
    #         elif dojos[-1].id != item['id']:
    #             new_dojo = Dojo(item)
    #             dojos.append(new_dojo)

    #         if item['ninjas.id'] != None:
    #             ninja_data = {
    #                 'id': item['ninjas.id'],
    #                 'first_name': item['first_name'],
    #                 'last_name': item['last_name'],
    #                 'age': item['age'],
    #                 'created_at': item['created_at'],
    #                 'updated_at': item['updated_at'],
    #                 'dojo_id': item['dojo_id'],
    #             }

    #             ninja = Ninja(ninja_data)
    #             ninja.dojo = new_dojo
    #             new_dojo.ninjas.append(ninja)

    #     return dojos