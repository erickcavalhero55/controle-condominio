from application.entity.person import PersonEntity
from application.repository.mysql import ConnectionManager, get_connection_manager


class PersonRepository:
    def __init__(self):
        self.connection = get_connection_manager().get_connection()

    def create(self, person: PersonEntity):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
                INSERT INTO person (
                    name,
                    email, 
                    phone
                ) 
                VALUES 
                (
                    '{person.name}',
                    '{person.email}',
                    '{person.phone}'
                )""")
        self.connection.commit()

        #Pega o ID que foi gerado com AUTO_INCREMENT no banco
        person.id = cursor.lastrowid

        return person

person_repository = PersonRepository()

def get_person_repository():
    return person_repository