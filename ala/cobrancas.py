from flask_restful import Resource, reqparse

cobrancas = [
    {
        'cobranca_id': 'a',
        'condominio': 320,
        'agua': 115,
        'luz': 150,
        'gas': 90
    },
    {
        'cobranca_id': 'b',
        'condominio': 320,
        'agua': 200,
        'luz': 180,
        'gas': 190
    },
    {
        'cobranca_id': 'c',
        'condominio': 320,
        'agua': 215,
        'luz': 120,
        'gas': 90
    }
]

class Cobrancas(Resource):
    def get(self):
        return {'cobrancas': cobrancas}

class Cobranca(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('condominio')
    argumentos.add_argument('agua')
    argumentos.add_argument('luz')
    argumentos.add_argument('gas')

    def find_cobranca(cobranca_id):
        for cobranca in cobrancas:
            if cobranca["cobranca_id"] == cobranca_id:
                return cobranca
        return None
    def get(self, cobranca_id):
        cobranca = Cobranca.find_cobranca(cobranca_id)
        if cobranca:
            return cobranca
        return {'message': 'Cobrancas not found:'}, 404

    def post(self, cobranca_id):

        dados = Cobranca.argumentos.parse_args()

        novo_cobranca = {
            'cobranca_id': cobranca_id,
            'condominio': dados['condominio'],
            'agua': dados['agua'],
            'luz': dados['luz'],
            'gas': dados['gas'],


        }

        cobrancas.append(novo_cobranca)
        return novo_cobranca, 200

    def put(self, cobranca_id):

        dados = Cobranca.argumentos.parse_args()
        novo_cobranca = {'cobranca_id': cobranca_id, **dados}

        cobranca = Cobranca.find_cobranca(cobranca_id)
        if cobranca:
            cobranca.update(novo_cobranca)
            return novo_cobranca, 200
        cobrancas.append(novo_cobranca)
        return novo_cobranca, 201

    def delete(self, cobranca_id):
        global cobrancas
        cobrancas = [cobranca for cobranca in cobrancas if cobranca['cobranca_id'] != cobranca_id]
        return {'message': 'Cobrancas deleted.'}