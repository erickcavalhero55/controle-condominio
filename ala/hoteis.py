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

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('cidade')

    def find_hotel(hoteis_id):
        for hotel in hoteis:
            if hotel["id_hoteis"] == hoteis_id:
                return hotel
        return None
    def get(self, hotel_id):
        hotel = Hotel.find.hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found:'}, 404

    def post(self, hotel_id):



        novo_hotel = {
            'id_hotel': hotel_id,
            'nome': dados['nome'],
            'cidade': dados['cidade']

        }

        hoteis.append(novo_hotel)
        return novo_hotel

    def put(self, hotel_id):

        dados  = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id': hotel_id, **dados}

        hoteis= Hotel.argumentos.parse_args()
        if hoteis:
            hoteis.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self):
        pass

