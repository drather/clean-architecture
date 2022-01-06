import pytest

from app.domain.entity import User
from app.infrastructure.database.orm import db, UserModel


# 기본 scope 는 function
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_database():
    # .db 파일을 남기지 않고, 메모리로 처리
    db.init(database=":memory:")

    db.connect()
    UserModel.create_table()


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name="grab")

    repository = UserRepository()
    created_user = repository.create(_user)

    user = repository.find_one(_user)
    assert user == created_user

