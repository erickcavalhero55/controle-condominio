import pymysql
from flask_restful import Resource, reqparse

unidades = [
    {
        'unidade_id': '1',
        'numero': 1,
        'bloco': 'a',
        'andar': 1
    },
    {
        'unidade_id': '2',
        'numero': 2,
        'bloco': 'b',
        'andar': 2
    },
    {
        'unidade_id': '3',
        'numero': 3,
        'bloco': 'c',
        'andar': 3
    }
]


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


def converte_rel_funcao(rel_funcao_converte):
    return {
        "id": rel_funcao_converte[0],
        "id_usuario": rel_funcao_converte[1],
        "id_funcao": rel_funcao_converte[2]
    }


class Rel_Funcaos(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM rel_funcao_usuario')
        rel_funcao = cursor.fetchall()

        if rel_funcao is None:
            return 404

        rel_funcao_convertido = []

        for rel_funcao in rel_funcao:
            rel_funcao_convertido.append(converte_rel_funcao(rel_funcao))

        return {'rel_funcao': rel_funcao_convertido}


class Rel_Funcao(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id_usuario')
    argumentos.add_argument('id_funcao')


    def get(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from rel_funcao_usuario where id ='{id}'")
        rel_funcao = cursor.fetchone()
        desconectar(conn)

        return converte_rel_funcao(rel_funcao)

    def post(self, id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Rel_Funcao.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO rel_funcao_usuario (id_usuario, id_funcao) VALUES ('{dados['id_usuario']}','{dados['id_funcao']}')")
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

        dados = Rel_Funcao.argumentos.parse_args()

        cursor.execute(
            f"UPDATE rel_funcao_usuario SET id_usuario='{dados['id_usuario']}',id_funcao='{dados['id_funcao']}' WHERE id = {id}")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def delete(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM rel_funcao_usuario')
        rel_funcoe = cursor.fetchall()

        if rel_funcoe is None:
            return 400

        cursor.execute(f'DELETE FROM rel_funcao_usuario WHERE id={id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Rel_Funcaos_Usuario excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)



