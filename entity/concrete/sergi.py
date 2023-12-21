from datetime import datetime

from entity.abstract import BaseEntity
from .eser import Eser


class Sergi(BaseEntity):
    def __init__(self, sergi_id: int, sergi_adi: str, sergi_tarihi: datetime, sergi_tipi: str,
                 sergi_aciklama, sergideki_eserler:list=[Eser]):
        self._sergi_id = sergi_id
        self._sergi_adi = sergi_adi
        self._sergi_tarihi = sergi_tarihi
        self._sergi_tipi = sergi_tipi
        self._sergi_aciklama = sergi_aciklama
        self._sergideki_eserler = sergideki_eserler

    def __str__(self):
        return f"Sergi Adı: {self._sergi_adi}\nTarih: {self._sergi_tarihi}\nTipi: {self._sergi_tipi}\n"

    @property
    def sergi_id(self):
        return self._sergi_id

    @property
    def sergi_adi(self):
        return self._sergi_adi

    @sergi_adi.setter
    def sergi_adi(self, yeni_deger):
        self._sergi_adi = yeni_deger

    @property
    def sergi_tipi(self):
        return self._sergi_tipi

    @sergi_tipi.setter
    def sergi_tipi(self, yeni_deger):
        self._sergi_tipi = yeni_deger

    @property
    def sergi_tarihi(self):
        return self._sergi_tarihi

    @sergi_tarihi.setter
    def sergi_tarihi(self, yeni_deger):
        self._sergi_tarihi = yeni_deger

    @property
    def sergi_aciklama(self):
        return self._sergi_aciklama

    @sergi_aciklama.setter
    def sergi_aciklama(self, yeni_deger):
        self._sergi_aciklama = yeni_deger

    @property
    def sergideki_eserler(self):
        return self._sergideki_eserler

    @sergideki_eserler.setter
    def sergideki_eserler(self, yeni_deger):
        self._sergideki_eserler = yeni_deger

