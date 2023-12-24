'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from abc import ABC, abstractmethod
from entity import Sergi, Eser


# ilgili sınıf için veri ekleme, silme, güncelleme, hepsini listeleme, idsi verileni alma gibi abstract metodların
# bulunduğu abstract sınıf
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

    @abstractmethod
    def delete_eser_from_sergi(self, eser_to_delete: Eser) -> None:
        pass
