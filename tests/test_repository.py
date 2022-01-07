import pytest

from app.domain.entity import User, Product
from app.infrastructure.database.orm import db, UserModel, ProductModel

# 기본 scope 는 function
from app.infrastructure.database.repository.product import ProductRepository
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_database():
    # .db 파일을 남기지 않고, 메모리로 처리
    db.init(database=":memory:")
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()


def test_create_user_repository(init_database):
    name = "grab"
    _user = User(name="grab")

    repository = UserRepository()
    created_user = repository.create(_user)

    user = repository.find_one(_user)
    assert user == created_user


def test_create_product(init_database):
    repository = ProductRepository()
    product_id, product_name, product_price = 1, "맥북", 1250000

    _product = Product(id=product_id, name=product_name, price=product_price)

    # Product 생성
    ProductModel.create(id=product_id, name=product_name, price=product_price)

    # Product 조회
    product = repository.find_one(model=_product)

    assert product.id == product_id and product.name == product_name and product.price == product_price

