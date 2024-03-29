import pymysql
from flask_restful import Resource, reqparse

from ala.conexao import conectar, desconectar


def converte_funcoes(funcoes_banco):
    return {
        "id": funcoes_banco[0],
        "funcao": funcoes_banco[1]
    }


class Funcoes(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funcoes')
        funcoes = cursor.fetchall()

        if funcoes is None:
            return 404

        funcoes_convertido = []

        for funcoe in funcoes:
            funcoes_convertido.append(converte_funcoes(funcoe))

        return {'funcoes': funcoes_convertido}


class Funcoe(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('funcao')


    def get(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from funcoes where id ='{id}'")
        funcoes = cursor.fetchone()

        return converte_funcoes(funcoes)

    def post(self, id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Funcoe.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO funcoes (funcao) VALUES ('{dados['funcao']}')")
        conn.commit()
        desconectar(conn)

        dados["id"] = cursor.lastrowid

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def put(self, id):

        conn = conectar()
        cursor = conn.cursor()

        dados = Funcoe.argumentos.parse_args()

        cursor.execute(
            f"UPDATE funcoes  SET funcao='{dados['funcao']}' WHERE id = '{id}'")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def delete(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM funcoes')
        funcoes = cursor.fetchall()

        if funcoes is None:
            return 400

        cursor.execute(f'DELETE FROM funcoes WHERE id={id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Funçoes excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)

