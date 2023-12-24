'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from entity import User
from ..abstract import AbcUserService
from data_access.abstract import AbcUserDal
from typing import override


# user ile ilgili veri erişim ve kullanıcı arayüzü arasındaki iş kodları katmanı
class UserService(AbcUserService):
    # user veri erişim katmanının referansını alıyor
    def __init__(self, user_dal: AbcUserDal):
        self._user_dal = user_dal

    # eğer eklenecek verinin idsi uygunsa veri erişim katmanına eklemesini söyler.
    @override
    def add(self, entity: User) -> None:
        if not self.get_by_id(entity.id):
            self._user_dal.add(entity)

    # eğer güncellenecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def update(self, entity: User) -> None:
        if self.get_by_id(entity.id):
            self._user_dal.update(entity)

    # eğer silinecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def delete(self, entity: User) -> None:
        if self.get_by_id(entity.id):
            self._user_dal.delete(entity)

    # veri erişim katmanından ilgili bütün verileri ister
    @override
    def get_all(self) -> list[User]:
        return self._user_dal.get_all()

    # veri erişim katmanından ilgili veriyi ister
    @override
    def get_by_id(self, id_param: int) -> User:
        return self._user_dal.get_by_id(id_param)