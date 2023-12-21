from abc import ABC, abstractmethod
from entity import Eser


class AbcEserService(ABC):
    @abstractmethod
    def add(self, entity: Eser) -> None:
        pass

    @abstractmethod
    def update(self, entity: Eser) -> None:
        pass

    @abstractmethod
    def delete(self, entity: Eser) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Eser]:
        pass

    @abstractmethod
    def get_by_id(self, id_param: int) -> Eser:
        pass
