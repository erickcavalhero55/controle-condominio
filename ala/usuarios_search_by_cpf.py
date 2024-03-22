import pymysql
from flask_restful import Resource, reqparse

from ala.conexao import conectar, desconectar


def converte_usuario(usuario_banco):
    return {
        "id": usuario_banco[0],
        "nome": usuario_banco[1],
        "sobrenome": usuario_banco[2],
        "rg": usuario_banco[3],
        "cpf": usuario_banco[4],
        "telefone": usuario_banco[5],
        "celular": usuario_banco[6],
        "email": usuario_banco[7],
        "genero": usuario_banco[8]
    }
class UsuariosSearchByCpf(Resource):
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
        usuario = cursor.fetchone()
        desconectar()

        if usuario is None:
            return {}, 404

        usuario_convertido = converte_usuario(usuario)

        return usuario_convertido
