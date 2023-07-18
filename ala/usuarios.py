import pymysql
from flask_restful import Resource, reqparse

pessoas = [
    {
        'pessoa_id': '1',
        'nome': 'Maria',
        'sobrenome': 'Dias',
        'rg': 123456789,
        'cpf': 789456123,
        'telefone': 1123456789,
        'celular': 11987654231,
        'email': 'Mariadias@gmail.com'

    },
    {
        'pessoa_id': '2',
        'nome': 'Joao',
        'sobrenome': 'Silva',
        'rg': 4564488961,
        'cpf': 56547899546,
        'telefone': 11125546985,
        'celular': 11954879859,
        'email': 'Joaosilva@gmail.com'

    },
    {
        'pessoa_id': '3',
        'nome': 'Jose',
        'sobrenome': 'Carvalho',
        'rg': 4578945625,
        'cpf': 45789546123,
        'telefone': 1124789456,
        'celular': 11945785123,
        'email': 'Josecarvalho@gmail.com'

    },
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


class Usuarios(Resource):
    def get(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()

        usuarios_convertido = []

        for usuario in usuarios:
            usuarios_convertido.append(converte_usuario(usuario))

        return {'usuarios': usuarios_convertido}


class Usuario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('rg')
    argumentos.add_argument('cpf')
    argumentos.add_argument('telefone')
    argumentos.add_argument('celular')
    argumentos.add_argument('email')
    argumentos.add_argument('genero')



    def get(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"select * from usuarios where id ='{id}'")
        usuario = cursor.fetchone()

        return converte_usuario(usuario)

    def post(self, id):
        conn = conectar()
        cursor = conn.cursor()

        dados = Usuario.argumentos.parse_args()

        cursor.execute(
            f"INSERT INTO usuarios (nome, sobrenome, rg, cpf, telefone, celular, email, genero) VALUES ('{dados['nome']}','{dados['sobrenome']}','{dados['rg']}','{dados['cpf']}','{dados['telefone']}','{dados['celular']}','{dados['email']}','{dados['genero']}')")
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

        dados = Usuario.argumentos.parse_args()

        cursor.execute(
            f"UPDATE usuarios SET nome='{dados['nome']}',sobrenome='{dados['sobrenome']}',rg='{dados['rg']}',cpf='{dados['cpf']}',telefone='{dados['telefone']}',celular='{dados['celular']}',email='{dados['email']}',genero='{dados['genero']} '")
        conn.commit()
        desconectar(conn)

        if cursor.rowcount == 1:
            return dados, 200
        else:
            return dados, 400

    def delete(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()

        if usuarios is None:
            return 400

        cursor.execute(f'DELETE FROM usuarios WHERE id={id}')
        conn.commit()

        if cursor.rowcount == 1:
            print('Usuarios excluido com sucesso.')
        else:
            print('Não foi possivel DELETAR. ')
        desconectar(conn)
