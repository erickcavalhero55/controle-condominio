import pymysql
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
def conectar():
    try:
        conn = pymysql.connect(
            db='controle_condominio',
            host='localhost',
            user='root',
            password='270921EN@'
        )
        return conn
    except pymysql.Error as e:
        print(f'Erro ao conectar ao Mysql {e}')


def desconectar(conn):
    if conn:
        conn.close()


class Funcoes(Resource):
    def get(self):
        return {'funcoes': funcoes}

class Funcoe(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('funcao')



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
        conn = conectar()
        cursor = conn.cursor()

        dados = Funcoe.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO funcoes (funcao) VALUES ('{dados['funcao']}')")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"A Funcoes {dados['funcao']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

        return dados, 200

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