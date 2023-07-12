import pymysql
from flask_restful import Resource, reqparse

veiculos = [
    {
        'veiculo_id': 'a',
        'placa': '1234',
        'marca': 'volvo ',
        'nome': 'volvo c40',
        'cor': 'preto'

    },
    {
        'veiculo_id': 'b',
        'placa': '1454',
        'marca': 'honda ',
        'nome': 'fit',
        'cor': 'branco'

    },
    {
        'veiculo_id': 'c',
        'placa': '1456',
        'marca': 'toyota ',
        'nome': 'corola',
        'cor': 'azul'

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

def converte_veiculo(veiculo_banco):
    return {
        "veiculo_id":veiculo_banco[0],
        "placa":veiculo_banco[1],
        "marca":veiculo_banco[2],
        "nome_veiculo":veiculo_banco[3],
        "cor":veiculo_banco[4],
        "id_usuarios":veiculo_banco[5]
    }

class Veiculos(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM veiculos')
        veiculos = cursor.fetchall()

        veiculos_convertido = []

        for veiculo in veiculos:
            veiculos_convertido.append(converte_veiculo(veiculo))

        return {'veiculos': veiculos_convertido}

class Veiculo(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('placa')
    argumentos.add_argument('marca')
    argumentos.add_argument('nome_veiculo')
    argumentos.add_argument('cor')
    argumentos.add_argument('id_usuarios')


    def find_veiculo(veiculo_id):
        for veiculo in veiculos:
            if veiculo["veiculo_id"] == veiculo_id:
                return veiculo
        return None
    def get(self, veiculo_id):
        veiculo = Veiculo.find_veiculo(veiculo_id)
        if veiculo:
            return veiculo
        return {'message': 'Veiculo not found:'}, 404

    def post(self, veiculo_id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Veiculo.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO veiculos (placa, marca, nome_veiculo, cor, id_usuarios) VALUES ('{dados['placa']}','{dados['marca']}','{dados['nome_veiculo']}','{dados['cor']}','{dados['id_usuarios']}')")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"O Veiculo {dados['placa']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

        return dados, 200

    def put(self, veiculo_id):

        dados = Veiculo.argumentos.parse_args()
        novo_veiculo = {'veiculo_id': veiculo_id, **dados}

        veiculo = Veiculo.find_veiculo(veiculo_id)
        if veiculo:
            veiculo.update(novo_veiculo)
            return novo_veiculo, 200
        veiculos.append(novo_veiculo)
        return novo_veiculo, 201

    def delete(self, veiculo_id):
        global veiculos
        veiculos = [veiculo for veiculo in veiculos if veiculo['veiculo_id'] != veiculo_id]
        return {'message': 'Veiculo deleted.'}