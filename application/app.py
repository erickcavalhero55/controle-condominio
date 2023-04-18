from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Portaria(Resource):
    def get(self):
        return {'portaria': 'cadastro'}

api.add_resource(Portaria, '/portaria')

if __name__== '__main__':
    app.run(debug=True)

