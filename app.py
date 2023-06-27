from flask import Flask
from flask_restful import Api
from ala.hoteis import Hoteis, Hotel
from ala.pessoas import Pessoas, Pessoa
from ala.unidades import Unidades, Unidade
from ala.encomendas import Encomendas, Encomenda

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<hotel_id>')
api.add_resource(Pessoas, '/pessoas')
api.add_resource(Pessoa, '/pessoa/<pessoa_id>')
api.add_resource(Unidades, '/unidades')
api.add_resource(Unidade, '/unidade/<unidade_id>')
api.add_resource(Encomendas, '/encomendas')
api.add_resource(Encomenda, '/encomenda/<id>')





if __name__ =='__main__':
    app.run(debug=True)
