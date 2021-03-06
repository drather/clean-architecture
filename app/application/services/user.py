from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import User


# 의존성 방향이 원 밖에서 원 안으로 흘러야 한다.
# 따라서, create_user 메서드 안에서 UserModel.save() 이런식으로 사용하면 안된다.
# (고수준이 저수준에 의존하게 됨)

class UserService:
    def __init__(self, user_repository: AbstractRepository):
        """
        repository 를 외부에서 주입받는 생성 메서드
        :param user_repository:
        """
        self.repository = user_repository

    def create_user(self, user_name: str):
        # user 객체 생성 후 DB 에 저장
        _user = User(name=user_name)

        # DB 에 해당 이름 있는지 확인하고, 있다면 Exception 발생
        if self.repository.find_one(model=_user):
            raise ValueError("유저가 이미 존재합니다")

        user = self.repository.create(_user)

        return user
