from application.entity.person import PersonEntity
from application.repository.person import get_person_repository


class PersonService:
    def __init__(self):
        self.person_repository = get_person_repository()

    def create(self, person: PersonEntity):
        return self.person_repository.create(person)


person_service = PersonService()


def get_person_service():
    return person_service
