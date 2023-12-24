'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from entity import Etkinlik
from ..abstract import AbcEtkinlikService
from data_access.abstract import AbcEtkinlikDal
from typing import override

# etkinlik ile ilgili veri erişim ve kullanıcı arayüzü arasındaki iş kodları katmanı
class EtkinlikService(AbcEtkinlikService):
    # etkinlik veri erişim katmanının referansını alıyor
    def __init__(self, etkinlik_dal: AbcEtkinlikDal):
        self._etkinlik_dal = etkinlik_dal

    # eğer eklenecek verinin idsi uygunsa veri erişim katmanına eklemesini söyler.
    @override
    def add(self, entity: Etkinlik) -> None:
        if not self.get_by_id(entity.etkinlik_id):
            self._etkinlik_dal.add(entity)

    # eğer güncellenecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def update(self, entity: Etkinlik) -> None:
        if self.get_by_id(entity.etkinlik_id):
            self._etkinlik_dal.update(entity)

    # eğer silinecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def delete(self, entity: Etkinlik) -> None:
        if self.get_by_id(entity.etkinlik_id):
            self._etkinlik_dal.delete(entity)

    # veri erişim katmanından ilgili bütün verileri ister

    @override
    def get_all(self) -> list[Etkinlik]:
        return self._etkinlik_dal.get_all()

    # veri erişim katmanından ilgili veriyi ister
    @override
    def get_by_id(self, id_param: int) -> Etkinlik:
        return self._etkinlik_dal.get_by_id(id_param)