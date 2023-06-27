from flask_restful import Resource, reqparse

veiculos = [
    {
        'veiculo_id': 'a',
        'placa': '1234',
        'marca': 'volvo ',
        'nome': 'volvo c40',
        'cor': 'preto'

    },
    {
        'veiculo_id': 'b',
        'placa': '1454',
        'marca': 'honda ',
        'nome': 'fit',
        'cor': 'branco'

    },
    {
        'veiculo_id': 'c',
        'placa': '1456',
        'marca': 'toyota ',
        'nome': 'corola',
        'cor': 'azul'

    }
]
class Veiculos(Resource):
    def get(self):
        return {'veiculos': veiculos}

class Veiculo(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('placa')
    argumentos.add_argument('marca')
    argumentos.add_argument('nome')
    argumentos.add_argument('cor')

    def find_veiculo(veiculo_id):
        for veiculo in veiculos:
            if veiculo["veiculo_id"] == veiculo_id:
                return veiculo
        return None
    def get(self, veiculo_id):
        veiculo = Veiculo.find_veiculo(veiculo_id)
        if veiculo:
            return veiculo
        return {'message': 'Veiculo not found:'}, 404

    def post(self, veiculo_id):

        dados = Veiculo.argumentos.parse_args()

        novo_veiculo = {
            'veiculo_id': veiculo_id,
            'placa': dados['placa'],
            'marca': dados['marca'],
            'nome': dados['nome'],
            'cor': dados['cor'],


        }

        veiculos.append(novo_veiculo)
        return novo_veiculo, 200

    def put(self, veiculo_id):

        dados = Veiculo.argumentos.parse_args()
        novo_veiculo = {'veiculo_id': veiculo_id, **dados}

        veiculo = Veiculo.find_veiculo(veiculo_id)
        if veiculo:
            veiculo.update(novo_veiculo)
            return novo_veiculo, 200
        veiculos.append(novo_veiculo)
        return novo_veiculo, 201

    def delete(self, veiculo_id):
        global veiculos
        veiculos = [veiculo for veiculo in veiculos if veiculo['veiculo_id'] != veiculo_id]
        return {'message': 'Veiculo deleted.'}