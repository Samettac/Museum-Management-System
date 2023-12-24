'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from abc import ABC, abstractmethod
from entity import Etkinlik


# ilgili sınıf için veri ekleme, silme, güncelleme, hepsini listeleme, idsi verileni alma gibi abstract metodların
# bulunduğu abstract sınıf
class AbcEtkinlikService(ABC):
    @abstractmethod
    def add(self, entity: Etkinlik) -> None:
        pass

    @abstractmethod
    def update(self, entity: Etkinlik) -> None:
        pass

    @abstractmethod
    def delete(self, entity: Etkinlik) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Etkinlik]:
        pass

    @abstractmethod
    def get_by_id(self, id_param: int) -> Etkinlik:
        pass
