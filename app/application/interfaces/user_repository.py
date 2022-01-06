import abc

from app.domain.entity import User, Domain


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, model: Domain):
        ...