'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''

from data_access.abstract import AbcEtkinlikDal
from entity import Etkinlik
from typing import override
from datetime import datetime

# etkinlik ile ilgili veri ekleme silme güncelleme ile ilgilenen katman
class MemoryEtkinlikDal(AbcEtkinlikDal):
    def __init__(self):
        # veri tabanı yerine etkinlikleri barındıran bir liste
        self._etkinlikler = [
            Etkinlik(etkinlik_id=1, etkinlik_adi="Çömlek Atölyesi", etkinlik_tarihi=datetime(2024, 1, 12),
                     etkinlik_aciklama="asdfghjklşçlk"),
            Etkinlik(etkinlik_id=2, etkinlik_adi="Resim Atölyesi", etkinlik_tarihi=datetime(2023, 12, 28),
                     etkinlik_aciklama="asdfghjklşçlk"),
            Etkinlik(etkinlik_id=3, etkinlik_adi="Kodlama Atölyesi", etkinlik_tarihi=datetime(2024, 1, 8),
                     etkinlik_aciklama="asdfghjklşçlk"),
            Etkinlik(etkinlik_id=4, etkinlik_adi="Yazarlık Atölyesi", etkinlik_tarihi=datetime(2024, 2, 1),
                     etkinlik_aciklama="asdfghjklşçlk"),
        ]

    # verilen etkinliği listeyee ekliyor
    @override
    def add(self, etkinlik_param: Etkinlik) -> None:
        self._etkinlikler.append(etkinlik_param)

    # verilen etkinliğin id'si ile aynı olan etkinliğin listedeki yerini bulur ve verilen etkinliğin bilgilerini günceller
    @override
    def update(self, etkinlik_param: Etkinlik) -> None:
        etkinlik_to_update = self.get_by_id(etkinlik_id=etkinlik_param.etkinlik_id)
        if etkinlik_to_update:
            index = self._etkinlikler.index(etkinlik_to_update)
            self._etkinlikler[index].etkinlik_adi = etkinlik_param.etkinlik_adi
            self._etkinlikler[index].etkinlik_tarihi = etkinlik_param.etkinlik_tarihi
            self._etkinlikler[index].etkinlik_aciklama = etkinlik_param.etkinlik_aciklama
        else:
            raise ValueError

    # verilen etkinliğin idsi geçerliyse etkinliğin listedeki yerini bulur ve verilen etkinliği siler
    @override
    def delete(self, etkinlik_param: Etkinlik) -> None:
        etkinlik_to_delete = self.get_by_id(etkinlik_id=etkinlik_param.etkinlik_id)
        if etkinlik_to_delete:
            self._etkinlikler.remove(etkinlik_to_delete)
        else:
            raise ValueError

    # bütün etkinlikleri döndürür
    @override
    def get_all(self) -> list[Etkinlik]:
        return self._etkinlikler

    # idsi verilen etkinlik varsa onu döndürür.
    @override
    def get_by_id(self, etkinlik_id: int) -> Etkinlik:
        for etkinlik in self.get_all():
            if etkinlik.etkinlik_id == etkinlik_id:
                return etkinlik
