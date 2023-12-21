from abc import ABC, abstractmethod
from entity import BaseEntity


class AbcEntityRepository[T: BaseEntity](ABC):
    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def get_by_id(self, id_param: int) -> T:
        pass