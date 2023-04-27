import uuid

from flask_restful import Resource, reqparse

from application.entity.person import PersonEntity

parser = reqparse.RequestParser()
parser.add_argument('name')

class PersonListResource(Resource):
    def get(self):
        return [
            {
                'id': "123",
                'name': "Erick",
            },
            {
                'id': "321",
                'name': "Renan",
            }
        ]
    def post(self):
        data = parser.parse_args()

        person = PersonEntity()
        person.name = data['name']


        return {
            'name': data['name']
        }
