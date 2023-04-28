import pymysql


class ConnectionManager:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                db='controle_condominio',
                host='172.16.1.3',
                user='root',
                password=''
            )
        return self.connection


connection_manager = ConnectionManager()


def get_connection_manager():
    return connection_manager
