from datetime import datetime

from data_access.abstract import AbcEserDal
from entity import Eser
from typing import override


class MemoryEserDal(AbcEserDal):
    def __init__(self):
        self._eserler = [
            Eser(eser_id=1, eser_adi="1984", eser_yazari="George Orwel", eser_tarihi=datetime(2015,1,10), eser_aciklama="distopya"),
            Eser(eser_id=2, eser_adi="Dune", eser_yazari="xxxx", eser_tarihi=datetime(2005,7,19), eser_aciklama="wow"),
            Eser(eser_id=3, eser_adi="harry potter", eser_yazari="J.K. Rowling", eser_tarihi=datetime(2002,1,10), eser_aciklama="fantastik"),
            Eser(eser_id=4, eser_adi="LoTR", eser_yazari="abc", eser_tarihi=datetime(1999,1,10), eser_aciklama="yyy"),
        ]

    @override
    def add(self, eser: Eser) -> None:
        self._eserler.append(eser)

    @override
    def update(self, eser_param: Eser) -> None:
        eser_to_update = self.get_by_id(eser_id=eser_param.eser_id)
        if eser_to_update:
            index = self._eserler.index(eser_to_update)
            self._eserler[index].eser_adi = eser_param.eser_adi
            self._eserler[index].eser_yazari = eser_param.eser_yazari
            self._eserler[index].eser_tarihi = eser_param.eser_tarihi
            self._eserler[index].eser_aciklama = eser_param.eser_aciklama
        else:
            raise ValueError

    @override
    def delete(self, eser_param: Eser) -> None:
        eser_to_delete = self.get_by_id(eser_id=eser_param.eser_id)
        if eser_to_delete:
            self._eserler.remove(eser_to_delete)
        else:
            raise ValueError

    @override
    def get_all(self) -> list[Eser]:
        return self._eserler

    @override
    def get_by_id(self, eser_id) -> Eser:
        for eser in self.get_all():
            if eser.eser_id == eser_id:
                return eser
