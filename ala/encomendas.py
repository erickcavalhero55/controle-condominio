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


class Encomendas(Resource):
    def get(self):
        return {'encomendas': encomendas}

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
        encomenda = Encomenda.find_encomenda(encomenda_id)
        if encomenda:
            return encomenda
        return {'message': 'Encomenda not found:'}, 404

    def post(self, encomenda_id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Encomenda.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO encomendas (titulo, tipo, nota_fiscal, id_usuarios) VALUES ('{dados['titulo']}','{dados['tipo']}','{dados['nota_fiscal']}','{dados['id_usuarios']}')")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"A Encomenda {dados['titulo']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

        return dados, 200

    def put(self, encomenda_id):

        dados = Encomenda.argumentos.parse_args()
        nova_encomenda = {'encomenda_id': encomenda_id, **dados}

        encomenda = Encomenda.find_encomenda(encomenda_id)
        if encomenda:
            encomenda.update(nova_encomenda)
            return nova_encomenda, 200
        encomendas.append(nova_encomenda)
        return nova_encomenda, 201

    def delete(self, encomenda_id):
        global encomendas
        encomendas = [encomenda for encomenda in encomendas if encomenda['encomenda_id'] != encomenda_id]
        return {'message': 'Encomenda deleted.'}

