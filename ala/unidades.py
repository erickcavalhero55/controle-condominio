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
            user='root',
            password='270921EN@'
        )
        return conn
    except pymysql.Error as e:
        print(f'Erro ao conectar ao Mysql {e}')


def desconectar(conn):
    if conn:
        conn.close()

def converte_unidade(unidade_banco):
    return {
        "unidade_id":unidade_banco[0],
        "numero":unidade_banco[1],
        "bloco":unidade_banco[2],
        "andar":unidade_banco[3],
        "id_usuarios":unidade_banco[4]
    }



class Unidades(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM unidades')
        unidades = cursor.fetchall()

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

    def find_unidade(unidade_id):
        for unidade in unidades:
            if unidade["unidade_id"] == unidade_id:
                return unidade
        return None

    def get(self, unidade_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from unidades where id ='{unidade_id}'")
        unidade = cursor.fetchone()

        return converte_unidade(unidade)
    def post(self, unidade_id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Unidade.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO unidades  (numero, bloco, andar, id_usuarios) VALUES ('{dados['numero']}','{dados['bloco']}','{dados['andar']}','{dados['id_usuarios']}')")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"A Unidade {dados['numero']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)


        return dados, 200

    def put(self, unidade_id):

        dados = Unidade.argumentos.parse_args()
        nova_unidade = {'unidade_id': unidade_id, **dados}

        unidade = Unidade.find_unidade(unidade_id)
        if unidade:
            unidade.update(nova_unidade)
            return nova_unidade, 200
        unidades.append(nova_unidade)
        return nova_unidade, 201

    def delete(self, unidade_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f'DELETE FROM unidades WHERE id={unidade_id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Unidades excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)
