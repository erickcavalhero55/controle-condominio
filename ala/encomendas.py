from flask_restful import Resource, reqparse

encomendas = [
    {
        'id': 1,
        'titulo': 'Mercado livre',
        'tipo': 'caixa',
        'codigo': 123245658


    },
    {
        'id': 2,
        'titulo': 'Amazon',
        'tipo': 'envelope',
        'codigo': 556589546


    },
    {
        'id': 3,
        'titulo': 'Casas Bahia',
        'tipo': 'carta',
        'codigo': 4578954645658111


    },
]
class Encomendas(Resource):
    def get(self):
        return {'encomendas': encomendas}

class Encomenda(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('titulo')
    argumentos.add_argument('tipo')
    argumentos.add_argument('codigo')


    def find_emcomenda(id):
        for encomenda in encomendas:
            if encomenda["id"] == id:
                return encomenda
        return None
    def get(self, id):
        encomenda = Encomenda.find_emcomenda(id)
        if encomenda:
            return encomenda
        return {'message': 'Encomenda not found:'}, 404

    def post(self, id):

        dados = Encomenda.argumentos.parse_args()

        nova_encomenda = {
            'id': id,
            'titulo': dados['titulo'],
            'tipo': dados['tipo'],
            'codigo': dados['codigo']


        }

        encomendas.append(nova_encomenda)
        return nova_encomenda, 200

    def put(self, id):

        dados = Encomenda.argumentos.parse_args()
        nova_encomenda = {'id': id, **dados}

        encomenda = Encomenda.find_emcomenda(id)
        if encomenda:
            encomenda.update(nova_encomenda)
            return nova_encomenda, 200
        encomendas.append(nova_encomenda)
        return nova_encomenda, 201

    def delete(self, pessoa_id):
        global encomendas
        encomendas = [encomenda for encomenda in encomendas if encomenda['id'] != id]
        return {'message': 'Encomenda deleted.'}

