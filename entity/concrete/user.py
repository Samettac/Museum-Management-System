'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''
from entity.abstract import BaseEntity
from entity.concrete import Sergi, Eser, Etkinlik
from flask_login import UserMixin

# User Sınıfının bütün özellikleri kapsülleme ile korunuyor ve methodları data access katmanında yer alıyor.
class User(BaseEntity, UserMixin):
    def __init__(self, id: int, kullanıcı_adi: str, kullanıcı_sifre: str):
        self._id = id
        self._kullanıcı_adi = kullanıcı_adi
        self._kullanıcı_sifre = kullanıcı_sifre

    @property
    def id(self):
        return self._id

    @property
    def kullanıcı_adi(self):
        return self._kullanıcı_adi

    @kullanıcı_adi.setter
    def kullanıcı_adi(self, yeni_deger: str):
        self._kullanıcı_adi = yeni_deger

    @property
    def kullanıcı_sifre(self):
        return self._kullanıcı_sifre

    @kullanıcı_sifre.setter
    def kullanıcı_sifre(self, yeni_deger: str):
        self._kullanıcı_sifre = yeni_deger
