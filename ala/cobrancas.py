import pymysql
from flask_restful import Resource, reqparse

cobrancas = [
    {
        'cobranca_id': 'a',
        'condominio': 320,
        'agua': 115,
        'luz': 150,
        'gas': 90   
    },
    {
        'cobranca_id': 'b',
        'condominio': 320,
        'agua': 200,
        'luz': 180,
        'gas': 190
    },
    {
        'cobranca_id': 'c',
        'condominio': 320,
        'agua': 215,
        'luz': 120,
        'gas': 90
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


class Cobrancas(Resource):
    def get(self):
        return {'cobrancas': cobrancas}

class Cobranca(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('cod_barras')
    argumentos.add_argument('data_vencimento')
    argumentos.add_argument('data_pagamento')
    argumentos.add_argument('valor')
    argumentos.add_argument('titulo')
    argumentos.add_argument('observacao')
    argumentos.add_argument('juros')
    argumentos.add_argument('multa')
    argumentos.add_argument('desconto')
    argumentos.add_argument('total')
    argumentos.add_argument('id_usuarios')

    def find_cobranca(cobranca_id):
        for cobranca in cobrancas:
            if cobranca["cobranca_id"] == cobranca_id:
                return cobranca
        return None
    def get(self, cobranca_id):
        cobranca = Cobranca.find_cobranca(cobranca_id)
        if cobranca:
            return cobranca
        return {'message': 'Cobrancas not found:'}, 404

    def post(self, cobranca_id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Cobranca.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO cobrancas (cod_barras, data_vencimento, data_pagamento, valor, titulo, observacao, juros, multa, desconto, total, id_usuarios) VALUES ('{dados['cod_barras']}','{dados['data_vencimento']}','{dados['data_pagamento']}','{dados['valor']}','{dados['titulo']}','{dados['observacao']}','{dados['juros']}','{dados['multa']}','{dados['desconto']}','{dados['total']}','{dados['id_usuarios']}')")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"A Cobranca {dados['cod_barras']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

        return dados, 200

    def put(self, cobranca_id):

        dados = Cobranca.argumentos.parse_args()
        novo_cobranca = {'cobranca_id': cobranca_id, **dados}

        cobranca = Cobranca.find_cobranca(cobranca_id)
        if cobranca:
            cobranca.update(novo_cobranca)
            return novo_cobranca, 200
        cobrancas.append(novo_cobranca)
        return novo_cobranca, 201

    def delete(self, cobranca_id):
        global cobrancas
        cobrancas = [cobranca for cobranca in cobrancas if cobranca['cobranca_id'] != cobranca_id]
        return {'message': 'Cobrancas deleted.'}