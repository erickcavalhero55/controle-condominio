from flask_restful import Resource, reqparse

funcoes = [
    {
        'funcoes_id': 'a',
        'nome': 'jose'


    },
    {
        'funcoes_id': 'b',
        'nome': 'maria'


    },
    {
        'funcoes_id': 'c',
        'nome': 'joao'


    }
]
class Funcoes(Resource):
    def get(self):
        return {'funcoes': funcoes}

class Funcoe(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')



    def find_funcoe(funcoes_id):
        for funcoe in funcoes:
            if funcoe["funcoes_id"] == funcoes_id:
                return funcoe
        return None

    def get(self, funcoes_id):
        funcoe = Funcoe.find_funcoe(funcoes_id)
        if funcoe:
            return funcoe
        return {'message': 'Funcoe not found:'}, 404

    def post(self, funcoes_id):

        dados = Funcoe.argumentos.parse_args()

        nova_funcoe = {
            'funcoes_id': funcoes_id,
            'nome': dados['nome'],


        }

        funcoes.append(nova_funcoe)
        return nova_funcoe, 200

    def put(self, funcoes_id):

        dados = Funcoe.argumentos.parse_args()
        nova_funcoe = {'funcoes_id': funcoes_id, **dados}

        funcoe = Funcoe.find_funcoe(funcoes_id)
        if funcoe:
            funcoe.update(nova_funcoe)
            return nova_funcoe, 200
        funcoes.append(nova_funcoe)
        return nova_funcoe, 201

    def delete(self, funcoes_id):
        global funcoes
        funcoes = [funcoe for funcoe in funcoes if funcoe['funcoes_id'] != funcoes_id]
        return {'message': 'Funcoes deleted.'}