import pymysql
from flask_restful import Resource, reqparse


def conectar():
    try:
        conn = pymysql.connect(
            db='controle_condominio',
            host='localhost',
            user='app',
            password='@Erick270921'
        )
        return conn
    except pymysql.Error as e:
        print(f'Erro ao conectar ao Mysql {e}')


def desconectar(conn):
    if conn:
        conn.close()


def converte_validacao(validacao_banco):
    return {
        "id": validacao_banco[0],
        "nome": validacao_banco[1],
        "sobrenome": validacao_banco[2],
        "rg": validacao_banco[3],
        "cpf": validacao_banco[4],
        "telefone": validacao_banco[5],
        "celular": validacao_banco[6],
        "email": validacao_banco[7],
        "genero": validacao_banco[8]

    }
class Validacao(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('rg')
    argumentos.add_argument('cpf')
    argumentos.add_argument('telefone')
    argumentos.add_argument('celular')
    argumentos.add_argument('email')
    argumentos.add_argument('genero')


    def get(self, cpf):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from usuarios where cpf ='{cpf}'")
        validacao = cursor.fetchall()

        if validacao is None:
            return 404

        validacao_convertido = []

        for validacao in validacao:
            validacao_convertido.append(converte_validacao(validacao))

        return {'validacao': validacao_convertido}
