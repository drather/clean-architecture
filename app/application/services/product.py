from app.application.interfaces.repository import AbstractRepository
from app.domain.entity import Product


class ProductService:
    def __init__(self, repository: AbstractRepository):
        """
        repository 를 외부에서 주입 받는 생성 메서드
        :param repository:
        """
        self.repository = repository

    def get_product(self, product_id: int):
        """
        상품 검색 메서드
        :param product_id:
        :return:
        """
        _product = Product(id=product_id)
        product = self.repository.find_one(model=_product)

        return product

    def get_product_all(self):
        """
        전체 조회 메서드
        :return:
        """
        all_products = self.repository.find_all()
        return all_products
