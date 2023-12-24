'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''

from entity import Eser
from ..abstract import AbcEserService
from data_access.abstract import AbcEserDal
from typing import override

# eser ile ilgili veri erişim ve kullanıcı arayüzü arasındaki iş kodları katmanı
class EserService(AbcEserService):
    # eserin veri erişim katmanının referansını alıyor
    def __init__(self, eser_dal: AbcEserDal):
        self._eser_dal = eser_dal

    # eğer eklenecek verinin idsi uygunsa veri erişim katmanına eklemesini söyler.
    @override
    def add(self, entity: Eser) -> None:
        if not self.get_by_id(entity.eser_id):
            self._eser_dal.add(entity)

    # eğer güncellenecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def update(self, entity: Eser) -> None:
        if self.get_by_id(entity.eser_id):
            self._eser_dal.update(entity)

    # eğer silinecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def delete(self, entity: Eser) -> None:
        if self._eser_dal.get_by_id(entity.eser_id):
            self._eser_dal.delete(entity)

    # veri erişim katmanından ilgili bütün verileri ister
    @override
    def get_all(self) -> list[Eser]:
        return self._eser_dal.get_all()

    # veri erişim katmanından ilgili veriyi ister
    @override
    def get_by_id(self, id_param: int) -> Eser:
        return self._eser_dal.get_by_id(id_param)