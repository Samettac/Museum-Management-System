'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from entity import Sergi, Eser
from ..abstract import AbcSergiService
from data_access.abstract import AbcSergiDal
from typing import override


# sergi ile ilgili veri erişim ve kullanıcı arayüzü arasındaki iş kodları katmanı
class SergiService(AbcSergiService):
    # sergi veri erişim katmanının referansını alıyor
    def __init__(self, sergi_dal: AbcSergiDal):
        self._sergi_dal = sergi_dal

    # eğer eklenecek verinin idsi uygunsa veri erişim katmanına eklemesini söyler.
    @override
    def add(self, entity: Sergi) -> None:
        if not self.get_by_id(entity.sergi_id):
            self._sergi_dal.add(entity)

    # eğer güncellenecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def update(self, entity: Sergi) -> None:
        if self.get_by_id(entity.sergi_id):
            self._sergi_dal.update(entity)

    # eğer silinecek verinin idsi varsa veri erişim katmanına güncellemesini söyler.
    @override
    def delete(self, entity: Sergi) -> None:
        if self.get_by_id(entity.sergi_id):
            self._sergi_dal.delete(entity)

    @override
    # veri erişim katmanından ilgili bütün verileri ister
    def get_all(self) -> list[Sergi]:
        return self._sergi_dal.get_all()

    # veri erişim katmanından ilgili veriyi ister
    @override
    def get_by_id(self, id_param: int) -> Sergi:
        return self._sergi_dal.get_by_id(id_param)

    # sergiden eser silmek için veri erişimde ilgili metodu ister
    @override
    def delete_eser_from_sergi(self, eser_to_delete: Eser) -> None:
        return self._sergi_dal.delete_eser_from_sergi(eser_to_delete)