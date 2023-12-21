from entity import Sergi
from ..abstract import AbcSergiService
from data_access.abstract import AbcSergiDal
from typing import override


class SergiService(AbcSergiService):
    def __init__(self, sergi_dal: AbcSergiDal):
        self._sergi_dal = sergi_dal

    @override
    def add(self, entity: Sergi) -> None:
        self._sergi_dal.add(entity)

    @override
    def update(self, entity: Sergi) -> None:
        self._sergi_dal.update(entity)

    @override
    def delete(self, entity: Sergi) -> None:
        self._sergi_dal.delete(entity)

    @override
    def get_all(self) -> list[Sergi]:
        return self._sergi_dal.get_all()

    @override
    def get_by_id(self, id_param: int) -> Sergi:
        return self._sergi_dal.get_by_id(id_param)