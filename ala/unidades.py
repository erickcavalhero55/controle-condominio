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


def converte_unidade(unidade_banco):
    return {
        "id": unidade_banco[0],
        "numero": unidade_banco[1],
        "bloco": unidade_banco[2],
        "andar": unidade_banco[3],
        "id_usuarios": unidade_banco[4]
    }


class Unidades(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM unidades')
        unidades = cursor.fetchall()

        if unidades is None:
            return 404

        unidades_convertido = []

        for unidade in unidades:
            unidades_convertido.append(converte_unidade(unidade))

        return {'unidade': unidades_convertido}


class Unidade(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('numero')
    argumentos.add_argument('bloco')
    argumentos.add_argument('andar')
    argumentos.add_argument('id_usuarios')


    def get(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from unidades where id ='{id}'")
        unidade = cursor.fetchone()
        desconectar(conn)

        return converte_unidade(unidade)

    def post(self, id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Unidade.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO unidades (numero, bloco, andar, id_usuarios) VALUES ('{dados['numero']}','{dados['bloco']}','{dados['andar']}','{dados['id_usuarios']}')")
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

        dados = Unidade.argumentos.parse_args()

        cursor.execute(
            f"UPDATE unidades SET numero='{dados['numero']}',bloco='{dados['bloco']}', andar='{dados['andar']}',id_usuarios='{dados['id_usuarios']}' WHERE id = {id}")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def delete(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM unidades')
        unidades = cursor.fetchall()

        if unidades is None:
            return 400

        cursor.execute(f'DELETE FROM unidades WHERE id={id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Unidades excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)


