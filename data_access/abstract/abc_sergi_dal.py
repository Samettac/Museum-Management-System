from abc import ABC, abstractmethod
from .abc_entity_repository import AbcEntityRepository
from entity import Sergi, Eser


class AbcSergiDal(AbcEntityRepository[Sergi], ABC):
    pass
    # @abstractmethod
    # def add_eser_to_sergi(self, sergi: Sergi, eser: Eser):
    #     pass
    #
    # @abstractmethod
    # def delete_eser_to_sergi(self, sergi: Sergi, eser: Eser):
    #     pass