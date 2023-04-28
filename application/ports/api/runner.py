from flask import Flask
from flask_restful import Api

from application.ports.api.resources.person import PersonResource
from application.ports.api.resources.person_list import PersonListResource


def start():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(PersonListResource, "/person")
    api.add_resource(PersonResource, "/person/<id>")

    app.run()
