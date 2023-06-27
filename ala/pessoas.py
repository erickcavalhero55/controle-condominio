from flask_restful import Resource, reqparse

pessoas = [
    {
        'pessoa_id': '1',
        'nome': 'Maria',
        'sobrenome': 'Dias',
        'rg': 123456789,
        'cpf': 789456123,
        'telefone': 1123456789,
        'celular': 11987654231,
        'email': 'Mariadias@gmail.com'

    },
    {
        'pessoa_id': '2',
        'nome': 'Joao',
        'sobrenome': 'Silva',
        'rg': 4564488961,
        'cpf': 56547899546,
        'telefone': 11125546985,
        'celular': 11954879859,
        'email': 'Joaosilva@gmail.com'

    },
    {
        'pessoa_id': '3',
        'nome': 'Jose',
        'sobrenome': 'Carvalho',
        'rg': 4578945625,
        'cpf': 45789546123,
        'telefone': 1124789456,
        'celular': 11945785123,
        'email': 'Josecarvalho@gmail.com'

    },
]

class Pessoas(Resource):
    def get(self):
        return {'pessoas': pessoas}

class Pessoa(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('rg')
    argumentos.add_argument('cpf')
    argumentos.add_argument('telefone')
    argumentos.add_argument('celular')
    argumentos.add_argument('email')

    def find_pessoa(pessoa_id):
        for pessoa in pessoas:
            if pessoa["pessoa_id"] == pessoa_id:
                return pessoa
        return None
    def get(self, pessoa_id):
        pessoa = Pessoa.find_pessoa(pessoa_id)
        if pessoa:
            return pessoa
        return {'message': 'Cadatro not found:'}, 404

    def post(self, pessoa_id):

        dados = Pessoa.argumentos.parse_args()

        novo_cadastro = {
            'pessoa_id': pessoa_id,
            'nome': dados['nome'],
            'sobrenome': dados['sobrenome'],
            'rg': dados['rg'],
            'cpf': dados['cpf'],
            'telefone': dados['telefone'],
            'celular': dados['celular'],
            'email': dados['email']

        }

        pessoas.append(novo_cadastro)
        return novo_cadastro, 200

    def put(self, pessoa_id):

        dados = Pessoa.argumentos.parse_args()
        novo_cadastro = {'pessoa_id': pessoa_id, **dados}

        pessoa = Pessoa.find_pessoa(pessoa_id)
        if pessoa:
            pessoa.update(novo_cadastro)
            return novo_cadastro, 200
        pessoas.append(novo_cadastro)
        return novo_cadastro, 201

    def delete(self, pessoa_id):
        global pessoas
        pessoas = [pessoa for pessoa in pessoas if pessoa['pessoa_id'] != pessoa_id]
        return {'message': 'Cadastro deleted.'}
