from flask_restful import Resource, reqparse

encomendas = [
    {
        'encomenda_id': 'a',
        'titulo': 'Mercado livre',
        'tipo': 'caixa',
        'codigo': 123245658


    },
    {
        'encomenda_id': 'b',
        'titulo': 'Amazon',
        'tipo': 'envelope',
        'codigo': 556589546


    },
    {
        'encomenda_id': 'c',
        'titulo': 'Casas Bahia',
        'tipo': 'carta',
        'codigo': 4578954645658111


    }
]
class Encomendas(Resource):
    def get(self):
        return {'encomendas': encomendas}

class Encomenda(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('titulo')
    argumentos.add_argument('tipo')
    argumentos.add_argument('codigo')


    def find_encomenda(encomenda_id):
        for encomenda in encomendas:
            if encomenda["encomenda_id"] == encomenda_id:
                return encomenda
        return None
    def get(self, encomenda_id):
        encomenda = Encomenda.find_encomenda(encomenda_id)
        if encomenda:
            return encomenda
        return {'message': 'Encomenda not found:'}, 404

    def post(self, encomenda_id):

        dados = Encomenda.argumentos.parse_args()

        nova_encomenda = {
            'encomenda_id': encomenda_id,
            'titulo': dados['titulo'],
            'tipo': dados['tipo'],
            'codigo': dados['codigo']


        }

        encomendas.append(nova_encomenda)
        return nova_encomenda, 200

    def put(self, encomenda_id):

        dados = Encomenda.argumentos.parse_args()
        nova_encomenda = {'encomenda_id': encomenda_id, **dados}

        encomenda = Encomenda.find_encomenda(encomenda_id)
        if encomenda:
            encomenda.update(nova_encomenda)
            return nova_encomenda, 200
        encomendas.append(nova_encomenda)
        return nova_encomenda, 201

    def delete(self, encomenda_id):
        global encomendas
        encomendas = [encomenda for encomenda in encomendas if encomenda['encomenda_id'] != encomenda_id]
        return {'message': 'Encomenda deleted.'}

