from entity import Eser
from ..abstract import AbcEserService
from data_access.abstract import AbcEserDal
from typing import override


class EserService(AbcEserService):
    def __init__(self, eser_dal: AbcEserDal):
        self._eser_dal = eser_dal

    @override
    def add(self, entity: Eser) -> None:
        self._eser_dal.add(entity)

    @override
    def update(self, entity: Eser) -> None:
        self._eser_dal.update(entity)

    @override
    def delete(self, entity: Eser) -> None:
        self._eser_dal.update(entity)

    @override
    def get_all(self) -> list[Eser]:
        return self._eser_dal.get_all()

    @override
    def get_by_id(self, id_param: int) -> Eser:
        return self._eser_dal.get_by_id(id_param)