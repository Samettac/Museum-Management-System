'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from abc import ABC, abstractmethod
from entity import BaseEntity


# Bu Abstrac Classta Generic Factory Mimarisi kullandık. T türünde verilen verinin ekleme, silme, güncelleme,
# hepsini listeleme
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