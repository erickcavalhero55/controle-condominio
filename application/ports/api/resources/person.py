from flask_restful import Resource


class PersonResource(Resource):
    def get(self, id):
        return {
            'id': id,
            'nome': "Renan",
        }
