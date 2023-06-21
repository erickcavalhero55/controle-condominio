from flask import Flask
from flask_restful import Api
from ala.hoteis import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<string:hoteis_id>')


if __name__ =='__main__':
    app.run(debug=True)
