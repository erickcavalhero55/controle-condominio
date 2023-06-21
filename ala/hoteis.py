from flask_restful import Resource, reqparse

hoteis = [
    {

        'id_hoteis': 'alfa',
        'nome': 'erick',
        'cidade': ' sao paulo'

    },
    {

        'id_hoteis': 'bravo',
        'nome': 'renan',
        'cidade': ' rio de janeiro'

    },
    {

        'id_hoteis': 'clarlie',
        'nome': 'enzo',
        'cidade': ' parana'

    }

]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    def get(self, hoteis_id):
        for hotel in hoteis:
            if hotel["id_hoteis"] == hoteis_id:
                return hotel
        return {'message': 'Hotel not found:'}, 404

    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
            'id_hotel': hotel_id,
            'nome': dados['nome'],
            'cidade': dados['cidade']

        }

        hoteis.append(novo_hotel)
        return novo_hotel

    def put(self):
        pass

    def delete(self):
        pass
