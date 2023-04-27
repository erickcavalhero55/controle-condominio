import pymysql


def conectar():
    try:
        conn = pymysql.connect(
            db='controle_condominio',
            host='172.16.1.3',
            user='root',
            password=''
        )
        return conn
    except pymysql.Error as e:
        print(f'Erro ao conectar ao Mysql {e}')
