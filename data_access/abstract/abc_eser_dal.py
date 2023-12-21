from abc import ABC
from .abc_entity_repository import AbcEntityRepository
from entity import Eser


class AbcEserDal(AbcEntityRepository[Eser], ABC):
    pass
