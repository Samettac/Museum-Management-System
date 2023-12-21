from abc import ABC
from .abc_entity_repository import AbcEntityRepository
from entity import Etkinlik


class AbcEtkinlikDal(AbcEntityRepository[Etkinlik], ABC):
    pass
