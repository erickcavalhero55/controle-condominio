import pymysql
from flask_restful import Resource, reqparse

from ala.conexao import conectar, desconectar

def converte_encomenda(encomenda_banco):
    return {"id": encomenda_banco[0], "titulo": encomenda_banco[1], "tipo": encomenda_banco[2],
            "nota_fiscal": encomenda_banco[3], "id_usuarios": encomenda_banco[4]}


class Encomendas(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM encomendas')
        encomendas = cursor.fetchall()

        if encomendas is None:
            return 404

        encomendas_convertido = []

        for encomenda in encomendas:
            encomendas_convertido.append(converte_encomenda(encomenda))

        return {'encomendas': encomendas_convertido}


class Encomenda(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('titulo')
    argumentos.add_argument('tipo')
    argumentos.add_argument('nota_fiscal')
    argumentos.add_argument('id_usuarios')




    def get(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from encomendas where id ='{id}'")
        encomenda = cursor.fetchone()

        return converte_encomenda(encomenda)

    def post(self, id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Encomenda.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO encomendas (titulo, tipo, nota_fiscal, id_usuarios) VALUES ('{dados['titulo']}','{dados['tipo']}','{dados['nota_fiscal']}','{dados['id_usuarios']}')")
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

        dados = Encomenda.argumentos.parse_args()

        cursor.execute(
            f"UPDATE encomendas SET titulo='{dados['titulo']}',tipo='{dados['tipo']}',nota_fiscal='{dados['nota_fiscal']}',id_usuarios='{dados['id_usuarios']}' WHERE id = '{id}'")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def delete(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM encomendas')
        encomendas = cursor.fetchall()

        if encomendas is None:
            return 400

        cursor.execute(f'DELETE FROM encomendas WHERE id={id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Encomendas excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)