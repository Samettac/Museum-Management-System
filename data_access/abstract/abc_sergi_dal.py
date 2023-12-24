'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''
from abc import ABC, abstractmethod
from .abc_entity_repository import AbcEntityRepository
from entity import Sergi, Eser

# generic entitiy repository'ye sergi sınıfı ile çalışacağını söylüyor ve onun sınıflarını kalıtım ile alıyor.
# ayrıca kendi fonksiyonu olan (bir eser silinindiğinde sergiden silme) abstackt metodu barındırıyor.
class AbcSergiDal(AbcEntityRepository[Sergi], ABC):

    @abstractmethod
    def delete_eser_from_sergi(self, eser_to_delete: Eser) -> None:
        pass