from entity.abstract import BaseEntity


class Etkinlik(BaseEntity):
    def __init__(self, etkinlik_adi: str, etkinlik_tarihi: str, etkinlik_katılımcıları: list, ):
        self._etkinlik_adi = etkinlik_adi
        self._etkinlik_tarihi = etkinlik_tarihi
        self._etkinlik_katılımcıları = etkinlik_katılımcıları

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
    def etkinlik_katılımcıları(self):
        return self._etkinlik_katılımcıları

    @etkinlik_katılımcıları.setter
    def etkinlik_katılımcıları(self, yeni_deger):
        self._etkinlik_katılımcıları = yeni_deger
