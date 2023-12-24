'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''
from entity.abstract import BaseEntity
from datetime import datetime


# Etkinlik Sınıfının bütün özellikleri kapsülleme ile korunuyor ve methodları data access katmanında yer alıyor.
class Etkinlik(BaseEntity):
    def __init__(self, etkinlik_id: int, etkinlik_adi: str, etkinlik_tarihi: datetime, etkinlik_aciklama: str):
        self._etkinlik_id = etkinlik_id
        self._etkinlik_adi = etkinlik_adi
        self._etkinlik_tarihi = etkinlik_tarihi
        self._etkinlik_aciklama = etkinlik_aciklama

    @property
    def etkinlik_id(self):
        return self._etkinlik_id

    @property
    def etkinlik_adi(self):
        return self._etkinlik_adi

    @etkinlik_adi.setter
    def etkinlik_adi(self, yeni_deger):
        self._etkinlik_adi = yeni_deger

    @property
    def etkinlik_tarihi(self):
        return self._etkinlik_tarihi

    @etkinlik_tarihi.setter
    def etkinlik_tarihi(self, yeni_deger):
        self._etkinlik_tarihi = yeni_deger

    @property
    def etkinlik_aciklama(self):
        return self._etkinlik_aciklama

    @etkinlik_aciklama.setter
    def etkinlik_aciklama(self, yeni_deger):
        self._etkinlik_aciklama = yeni_deger
