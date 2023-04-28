from flask_restful import Resource, reqparse

from application.entity.person import PersonEntity
from application.service.person import get_person_service

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('phone')
parser.add_argument('email')


class PersonListResource(Resource):
    def __init__(self):
        self.person_service = get_person_service()

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
        person.phone = data['phone']
        person.email = data['email']

        created_person = self.person_service.create(person)

        return created_person.toJSON()
