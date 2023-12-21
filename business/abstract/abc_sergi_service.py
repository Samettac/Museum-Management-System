from abc import ABC, abstractmethod
from entity import Sergi


class AbcSergiService(ABC):
    @abstractmethod
    def add(self, entity: Sergi) -> None:
        pass

    @abstractmethod
    def update(self, entity: Sergi) -> None:
        pass

    @abstractmethod
    def delete(self, entity: Sergi) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Sergi]:
        pass

    @abstractmethod
    def get_by_id(self, id_param: int) -> Sergi:
        pass
