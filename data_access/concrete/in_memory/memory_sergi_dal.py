'''204210770 Rohullah Ghafoori
204210786 Sayed suliman Torabi
234210076 Samet Tasci'''


from datetime import datetime

from data_access.abstract import AbcSergiDal
from entity import Sergi, Eser
from typing import override

# sergi ile ilgili veri ekleme silme güncelleme ile ilgilenen katman
class MemorySergiDal(AbcSergiDal):
    def __init__(self):
        # veri tabanı yerine sergileri barındıran bir liste
        self._sergiler = [
            Sergi(sergi_id=1, sergi_adi="eski araçlar", sergi_tipi="Tematik", sergi_tarihi=datetime(2015,1,10), sergi_aciklama="eski araçlar sergisi",
                  sergideki_eserler=[
                      Eser(eser_id=1, eser_adi="1984", eser_yazari="George Orwel", eser_tarihi=datetime(2015, 1, 10),
                           eser_aciklama="distopya"),
                      Eser(eser_id=2, eser_adi="Dune", eser_yazari="xxxx", eser_tarihi=datetime(2005, 7, 19),
                           eser_aciklama="wow"),
                      Eser(eser_id=3, eser_adi="harry potter", eser_yazari="J.K. Rowling",
                           eser_tarihi=datetime(2002, 1, 10), eser_aciklama="fantastik"),
                      Eser(eser_id=4, eser_adi="LoTR", eser_yazari="abc", eser_tarihi=datetime(1999, 1, 10),
                           eser_aciklama="yyy"),
        ]),
            Sergi(sergi_id=2, sergi_adi="aaa", sergi_tipi="Geçici", sergi_tarihi=datetime(2015,1,10), sergi_aciklama="aaa sergisi",
                  sergideki_eserler=[
                      Eser(eser_id=1, eser_adi="1984", eser_yazari="George Orwel", eser_tarihi=datetime(2015, 1, 10),
                           eser_aciklama="distopya"),
                      Eser(eser_id=2, eser_adi="Dune", eser_yazari="xxxx", eser_tarihi=datetime(2005, 7, 19),
                           eser_aciklama="wow"),
                      Eser(eser_id=3, eser_adi="harry potter", eser_yazari="J.K. Rowling",
                           eser_tarihi=datetime(2002, 1, 10), eser_aciklama="fantastik"),
        ]),
            Sergi(sergi_id=3, sergi_adi="bbb", sergi_tipi="Daimi", sergi_tarihi=datetime(2015,1,10), sergi_aciklama="bbb sergisi",
                  sergideki_eserler=[
                      Eser(eser_id=1, eser_adi="1984", eser_yazari="George Orwel", eser_tarihi=datetime(2015, 1, 10),
                           eser_aciklama="distopya"),
                      Eser(eser_id=2, eser_adi="Dune", eser_yazari="xxxx", eser_tarihi=datetime(2005, 7, 19),
                           eser_aciklama="wow"),
                      Eser(eser_id=4, eser_adi="LoTR", eser_yazari="abc", eser_tarihi=datetime(1999, 1, 10),
                           eser_aciklama="yyy"),
        ]),
            Sergi(sergi_id=4, sergi_adi="ccc", sergi_tipi="Tematik", sergi_tarihi=datetime(2015,1,10), sergi_aciklama="ccc sergisi",
                  sergideki_eserler=[
                      Eser(eser_id=2, eser_adi="Dune", eser_yazari="xxxx", eser_tarihi=datetime(2005, 7, 19),
                           eser_aciklama="wow"),
                      Eser(eser_id=3, eser_adi="harry potter", eser_yazari="J.K. Rowling",
                           eser_tarihi=datetime(2002, 1, 10), eser_aciklama="fantastik"),
                      Eser(eser_id=4, eser_adi="LoTR", eser_yazari="abc", eser_tarihi=datetime(1999, 1, 10),
                           eser_aciklama="yyy"),
        ]),
        ]

    # verilen serginin listeyee ekliyor
    @override
    def add(self, sergi: Sergi) -> None:
        self._sergiler.append(sergi)

    # verilen serginin id'si ile aynı olan serginin listedeki yerini bulur ve verilen serginin bilgilerini günceller
    @override
    def update(self, sergi_param: Sergi) -> None:
        sergi_to_update = self.get_by_id(sergi_id=sergi_param.sergi_id)
        if sergi_to_update:
            index = self._sergiler.index(sergi_to_update)
            self._sergiler[index].sergi_adi = sergi_param.sergi_adi
            self._sergiler[index].sergi_tipi = sergi_param.sergi_tipi
            self._sergiler[index].sergi_tarihi = sergi_param.sergi_tarihi
            self._sergiler[index].sergi_aciklama = sergi_param.sergi_aciklama
            self._sergiler[index].sergideki_eserler = sergi_param.sergideki_eserler
        else:
            raise ValueError

    # verilen serginin idsi geçerliyse serginin listedeki yerini bulur ve verilen sergiyi siler
    @override
    def delete(self, sergi_param: Sergi) -> None:
        sergi_to_delete = self.get_by_id(sergi_id=sergi_param.sergi_id)
        if sergi_to_delete:
            self._sergiler.remove(sergi_to_delete)
        else:
            raise ValueError

    # bütün sergileri döndürür
    @override
    def get_all(self) -> list[Sergi]:
        return self._sergiler

    # idsi verilen sergi varsa onu döndürür.
    @override
    def get_by_id(self, sergi_id) -> Sergi:
        for sergi in self.get_all():
            if sergi.sergi_id == sergi_id:
                return sergi

    # silinecek eser sergide varsa onu sergiden de siler.
    @override
    def delete_eser_from_sergi(self, eser_to_delete: Eser) -> None:
        for sergi in self.get_all():
            for eser in sergi.sergideki_eserler:
                if eser.eser_id == eser_to_delete.eser_id:
                    sergi.sergideki_eserler.remove(eser)
