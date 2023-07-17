import datetime

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

def converte_cobranca(cobranca_banco):
    return {
        "cobranca_id": cobranca_banco[0],
        "cod_barras": cobranca_banco[1],
        "data_vencimento":  cobranca_banco[2].strftime("%Y-%m-%d"),
        "data_pagamento": cobranca_banco[3].strftime("%Y-%m-%d %H:%M:%S"),
        "valor":cobranca_banco[4],
        "titulo":cobranca_banco[5],
        "observacao":cobranca_banco[6],
        "juros":cobranca_banco[7],
        "multa":cobranca_banco[8],
        "desconto":cobranca_banco[9],
        "total":cobranca_banco[10],
        "id_usuarios":cobranca_banco[11]
    }

class Cobrancas(Resource):

    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cobrancas')
        cobrancas = cursor.fetchall()

        cobrancas_convertido = []

        for cobranca in cobrancas:
           cobrancas_convertido.append(converte_cobranca(cobranca))

        return {'cobrancas': cobrancas_convertido}

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
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from cobrancas where id ='{cobranca_id}'")
        cobrancas = cursor.fetchone()

        return converte_cobranca(cobrancas)


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

        conn = conectar()
        cursor = conn.cursor()

        dados = cobranca.argumentos.parse_args()

        cursor.execute(
            f"UPDATE cobrancas SET cod_barras='{dados['cod_barras']}',data_vencimento='{dados['data_vencimento']}',nome_veiculo='{dados['nome_veiculo']}',cor='{dados['cor']}',id_usuarios='{dados['id_usuarios']}' WHERE id = '{veiculo_id}'")
        conn.commit()

        if cursor.rowcount == 1:
            print(f"O Veiculo {dados['placa']} foi inserido com sucesso. ")
        else:
            print('Não foi possivel cadastrar ')
        desconectar(conn)

    def delete(self, cobranca_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f'DELETE FROM cobrancas WHERE id={cobranca_id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Cobrancas excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)

