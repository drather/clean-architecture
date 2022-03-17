import abc

from app.domain.entity import User, Domain


"""
고수준 구현체 Repository
"""
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, model: Domain):
        """
        생성 메서드
        :param model:
        :return:
        """
        ...

    @abc.abstractmethod
    def find_one(self, model:Domain):
        """
        검색 메서드
        :param model:
        :return:
        """
        ...

    @abc.abstractmethod
    def find_all(self):
        """
        전체 조회 메서드
        :return:
        """
        ...