'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from data_access.abstract import AbcUserDal
from entity import User
from typing import override
from datetime import datetime

# kullanıcı ile ilgili veri ekleme silme güncelleme ile ilgilenen katman
class MemoryUserDal(AbcUserDal):
    # veri tabanı yerine kullanıcıları barındıran bir liste
    def __init__(self):
        self._userler = [
            User(id=1, kullanıcı_adi="admin", kullanıcı_sifre="admin"),
        ]

    # verilen eseri listeyee ekliyor
    @override
    def add(self, user_param: User) -> None:
        self._userler.append(user_param)


    # verilen kullanıcının id'si ile aynı olan kullanıcının listedeki yerini bulur ve verilen kullanıcıyı bilgilerini günceller
    @override
    def update(self, user_param: User) -> None:
        user_to_update = self.get_by_id(id=user_param.id)
        if user_to_update:
            index = self._userler.index(user_to_update)
            self._userler[index].kullanıcı_adi = user_param.kullanıcı_adi
            self._userler[index].kullanıcı_sifre = user_param.kullanıcı_sifre
        else:
            raise ValueError


    # verilen kullanıcının idsi geçerliyse kullanıcının listedeki yerini bulur ve verilen kullanıcıyı siler
    @override
    def delete(self, user_param: User) -> None:
        user_to_delete = self.get_by_id(id=user_param.id)
        if user_to_delete:
            self._userler.remove(user_to_delete)
        else:
            raise ValueError


    # bütün kullanıcıları döndürür
    @override
    def get_all(self) -> list[User]:
        return self._userler


    # idsi verilen kullanıcı varsa onu döndürür.
    @override
    def get_by_id(self, id: int) -> User:
        for user in self.get_all():
            if user.id == id:
                return user
