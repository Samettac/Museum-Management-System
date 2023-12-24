'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''

from abc import ABC
from .abc_entity_repository import AbcEntityRepository
from entity import User

# generic entitiy repository'ye user sınıfı ile çalışacağını söylüyor ve onun sınıflarını kalıtım ile alıyor.
class AbcUserDal(AbcEntityRepository[User], ABC):
    pass
