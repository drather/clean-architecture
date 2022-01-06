from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import User


# 의존성 방향이 원 밖에서 원 안으로 흘러야 한다.
# 따라서, create_user 메서드 안에서 UserModel.save() 이런식으로 사용하면 안된다.
# (고수준이 저수준에 의존하게 됨)

class UserService:
    def __init__(self, user_repository: AbstractRepository):
        self.repository = user_repository

    def create_user(self, user_name: str):
        # DB 에 저장
        _user = User(name=user_name)
        user = self.repository.create(_user)
        return user
