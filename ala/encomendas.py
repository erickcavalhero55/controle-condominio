import pymysql
from flask_restful import Resource, reqparse

encomendas = [
    {
        'encomenda_id': 'a',
        'titulo': 'Mercado livre',
        'tipo': 'caixa',
        'codigo': 123245658


    },
    {
        'encomenda_id': 'b',
        'titulo': 'Amazon',
        'tipo': 'envelope',
        'codigo': 556589546


    },
    {
        'encomenda_id': 'c',
        'titulo': 'Casas Bahia',
        'tipo': 'carta',
        'codigo': 4578954645658111


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

def converte_encomenda(encomenda_banco):
    return {
        "encomenda_id":encomenda_banco[0],
        "titulo":encomenda_banco[1],
        "tipo":encomenda_banco[2],
        "nota_fiscal":encomenda_banco[3],
        "id_usuarios":encomenda_banco[4]
    }


class Encomendas(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM encomendas')
        encomendas = cursor.fetchall()

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


    def find_encomenda(encomenda_id):
        for encomenda in encomendas:
            if encomenda["encomenda_id"] == encomenda_id:
                return encomenda
        return None
    def get(self, encomenda_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from encomendas where id ='{encomenda_id}'")
        encomenda = cursor.fetchone()

        return converte_encomenda(encomenda)



    def post(self, encomenda_id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Encomenda.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO encomendas (titulo, tipo, nota_fiscal, id_usuarios) VALUES ('{dados['titulo']}','{dados['tipo']}','{dados['nota_fiscal']}','{dados['id_usuarios']}')")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400


    def put(self, encomenda_id):

        conn = conectar()
        cursor = conn.cursor()

        dados = Encomenda.argumentos.parse_args()

        cursor.execute(
            f"UPDATE encomendas SET titulo='{dados['titulo']}',tipo='{dados['tipo']}',nota_fiscal='{dados['nota_fiscal']}',id_usuarios='{dados['id_usuarios']}' WHERE id = '{encomenda_id}'")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400


    def delete(self, encomenda_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f'DELETE FROM encomendas WHERE id={encomenda_id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Encomenda excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)
