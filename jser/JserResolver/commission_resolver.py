import os
from abc import ABC, abstractmethod

from jser.constant import HandlerType


class CommissionResolver(ABC):
    def __init__(self):
        self._niche_commission_data: dict = self.__template_niche_commission_data()

    def __template_niche_commission_data(self) -> dict[str, any]:
        commission_input_path = self._get_commission_input_path()
        commission_output_path = self._get_commission_output_path()
        if not os.path.exists(commission_output_path):
            self.update_niche_commission_file(commission_input_path, commission_output_path)
        return self.get_commission_data(commission_output_path)

    @abstractmethod
    def _get_commission_output_path(self) -> str:
        pass

    @abstractmethod
    def _get_commission_input_path(self) -> str:
        pass

    @abstractmethod
    def update_niche_commission_file(self, input_path: str, output_path: str) -> None:
        pass

    @abstractmethod
    def get_commission_data(self, path) -> dict[str, any]:
        pass

    @abstractmethod
    def _get_commission_for_niche(self, niche_name: str) -> dict[str, float]:
        pass

    @abstractmethod
    def get_commission_for_niche_mapped(self, niche_name: str) -> dict[HandlerType, float]:
        pass

    @abstractmethod
    def get_return_percent_for(self, niche_name: str) -> float:
        pass
