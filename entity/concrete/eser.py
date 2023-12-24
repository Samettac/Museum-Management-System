'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''
from datetime import datetime

from entity.abstract import BaseEntity

# Eser Sınıfının bütün özellikleri kapsülleme ile korunuyor ve methodları data access katmanında yer alıyor.
class Eser(BaseEntity):
    def __init__(self, eser_id: int, eser_adi: str, eser_yazari: str,
                 eser_tarihi: datetime, eser_aciklama: str):
        self._eser_id = eser_id
        self._eser_adi = eser_adi
        self._eser_yazari = eser_yazari
        self._eser_tarihi = eser_tarihi
        self._eser_aciklama = eser_aciklama

    def __str__(self):
        return (f"Eser ID: {self.eser_id}\nAdı: {self.eser_adi}\nYazar: {self.eser_yazari}\n"
                f"Tarih: {self.eser_tarihi}\nAçıklama: {self.eser_aciklama}\n")

    @property
    def eser_id(self):
        return self._eser_id

    @property
    def eser_adi(self):
        return self._eser_adi

    @eser_adi.setter
    def eser_adi(self, yeni_deger):
        self._eser_adi = yeni_deger

    @property
    def eser_yazari(self):
        return self._eser_yazari

    @eser_yazari.setter
    def eser_yazari(self, yeni_deger):
        self._eser_yazari = yeni_deger

    @property
    def eser_tarihi(self):
        return self._eser_tarihi

    @eser_tarihi.setter
    def eser_tarihi(self, yeni_deger):
        self._eser_tarihi = yeni_deger

    @property
    def eser_aciklama(self):
        return self._eser_aciklama

    @eser_aciklama.setter
    def eser_aciklama(self, yeni_deger):
        self._eser_aciklama = yeni_deger
