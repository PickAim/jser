import os
from abc import ABC, abstractmethod

from jorm.market.infrastructure import HandlerType

from jser.constant import COMMISSION_WILDBERRIES_BINARY
from jser.niche.commission.serialize_niche_commission import update_niche_commission_file, get_commission_data


class JserCommissionResolver(ABC):
    def __init__(self):
        self._niche_commission_data: dict = self.__template_get_niche_commission_data()

    def __template_get_niche_commission_data(self) -> dict[str, any]:
        if not os.path.exists(COMMISSION_WILDBERRIES_BINARY):
            update_niche_commission_file(COMMISSION_WILDBERRIES_BINARY)
        return get_commission_data()

    @abstractmethod
    def _get_commission_for_niche(self, niche_name: str) -> dict[str, float]:
        pass

    @abstractmethod
    def get_commission_for_niche_mapped(self, niche_name: str) -> dict[HandlerType: float]:
        pass

    @abstractmethod
    def get_return_percent_for(self, niche_name: str) -> float:
        pass
