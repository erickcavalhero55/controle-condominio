from flask_restful import Resource, reqparse

unidades = [
    {
        'unidade_id': '1',
        'numero': 1,
        'bloco': 'a',
        'andar': 1
    },
    {
        'unidade_id': '2',
        'numero': 2,
        'bloco': 'b',
        'andar': 2
    },
    {
        'unidade_id': '3',
        'numero': 3,
        'bloco': 'c',
        'andar': 3
    }
]

class Unidades(Resource):
    def get(self):
        return {'unidades': unidades}

class Unidade(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('numero')
    argumentos.add_argument('bloco')
    argumentos.add_argument('andar')

    def find_unidade(unidade_id):
        for unidade in unidades:
            if unidade["unidade_id"] == unidade_id:
                return unidade
        return None

    def get(self, unidade_id):
        unidade = Unidade.find_unidade(unidade_id)
        if unidade:
            return unidade
        return {'message': 'Unidade not found:'}, 404

    def post(self, unidade_id):

        dados = Unidade.argumentos.parse_args()

        nova_unidade = {
            'unidade_id': unidade_id,
            'numero': dados['numero'],
            'bloco': dados['bloco'],
            'andar': dados['andar']


        }

        unidades.append(nova_unidade)
        return nova_unidade, 200

    def put(self, unidade_id):

        dados = Unidade.argumentos.parse_args()
        nova_unidade = {'unidade_id': unidade_id, **dados}

        unidade = Unidade.find_unidade(unidade_id)
        if unidade:
            unidade.update(nova_unidade)
            return nova_unidade, 200
        unidades.append(nova_unidade)
        return nova_unidade, 201

    def delete(self, unidade_id):
        global unidades
        unidades = [unidade for unidade in unidades if unidade['unidade_id'] != unidade_id]
        return {'message': 'Unidade deleted.'}
