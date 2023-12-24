'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''

from abc import ABC, abstractmethod
from entity import Eser


# ilgili sınıf için veri ekleme, silme, güncelleme, hepsini listeleme, idsi verileni alma gibi abstract metodların
# bulunduğu abstract sınıf
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
