from flask import Flask
from flask_restful import Api
from ala.hoteis import Hoteis, Hotel
from ala.usuarios import Usuarios, Usuario
from ala.unidades import Unidades, Unidade
from ala.encomendas import Encomendas, Encomenda
from ala.funcoes import Funcoes, Funcoe
from ala.veiculos import Veiculos, Veiculo
from ala.cobrancas import Cobrancas, Cobranca

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hotel/<hotel_id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<id>')
api.add_resource(Unidades, '/unidades')
api.add_resource(Unidade, '/unidade/<unidade_id>')
api.add_resource(Encomendas, '/encomendas')
api.add_resource(Encomenda, '/encomenda/<encomenda_id>')
api.add_resource(Funcoes, '/funcoes')
api.add_resource(Funcoe, '/funcoe/<funcoes_id>')
api.add_resource(Veiculos, '/veiculos')
api.add_resource(Veiculo, '/veiculo/<veiculo_id>')
api.add_resource(Cobrancas, '/cobrancas')
api.add_resource(Cobranca, '/cobranca/<cobranca_id>')




if __name__ =='__main__':
    app.run(debug=True, port=80)
