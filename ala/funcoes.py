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

def converte_funcoes(funcoes_banco):
    return {
        "funcoes_id":funcoes_banco[0],
        "funcao":funcoes_banco[1]
    }


class Funcoes(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funcoes')
        funcoes = cursor.fetchall()

        funcoes_convertido = []

        for funcoe in funcoes:
            funcoes_convertido.append(converte_funcoes(funcoe))

        return {'funcoes': funcoes_convertido}

class Funcoe(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('funcao')



    def find_funcoe(funcoes_id):
        for funcoe in funcoes:
            if funcoe["funcoes_id"] == funcoes_id:
                return funcoe
        return None

    def get(self, funcoes_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from funcoes where id ='{funcoes_id}'")
        funcoes = cursor.fetchone()

        return converte_funcoes(funcoes)

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

        conn = conectar()
        cursor = conn.cursor()

        dados = funcoes.argumentos.parse_args()

        cursor.execute(
            f"UPDATE funcoes  SET funcao='{dados['funcao']}' WHERE id = '{funcoes_id}'")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"O Funçôes {dados['funcao']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

    def delete(self, funcoes_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f'DELETE FROM funcoes WHERE id={funcoes_id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Funçoes excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)