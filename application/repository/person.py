from application.entity.person import PersonEntity
from application.repository.mysql import conectar

conn = conectar()

def create(person: PersonEntity):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            INSERT INTO person (
                id, 
                name,
                email, 
                phone
            ) 
            VALUES 
            (
                {person.id},
                {person.name},
                {person.email},
                {person.phone}
            )""")
    conn.commit()

    return cursor.rowcount == 1
