from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import Domain


class FakeUserRepository(AbstractRepository):
    def __init__(self):
        self.users = []

    def create(self, model: Domain):
        self.users.append(model)
        return model

    def find_one(self, model: Domain):
        for _user in self.users:
            if _user.name == model.name:
                return model

        return None
