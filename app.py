from flask import Flask
from flask_restful import Api

from ala.cobrancas import Cobrancas, Cobranca
from ala.encomendas import Encomendas, Encomenda
from ala.funcoes import Funcoes, Funcoe
from ala.rel_funcao import Rel_Funcaos, Rel_Funcao
from ala.unidades import Unidades, Unidade
from ala.usuarios import Usuarios, Usuario
from ala.veiculos import Veiculos, Veiculo
from ala.usuarios_search_by_cpf import UsuariosSearchByCpf
app = Flask(__name__)
api = Api(app)

api.add_resource(Rel_Funcaos, '/rel_funcaos')
api.add_resource(Rel_Funcao, '/rel_funcao/<id>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<id>')
api.add_resource(UsuariosSearchByCpf, '/usuario/search-by-cpf/<cpf>')
api.add_resource(Unidades, '/unidades')
api.add_resource(Unidade, '/unidade/<id>')
api.add_resource(Encomendas, '/encomendas')
api.add_resource(Encomenda, '/encomenda/<id>')
api.add_resource(Funcoes, '/funcoes')
api.add_resource(Funcoe, '/funcoe/<id>')
api.add_resource(Veiculos, '/veiculos')
api.add_resource(Veiculo, '/veiculo/<id>')
api.add_resource(Cobrancas, '/cobrancas')
api.add_resource(Cobranca, '/cobranca/<id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
