import os
from abc import ABC, abstractmethod


class InformationResolver(ABC):
    def __init__(self):
        self._mapped_warehouses_data: dict = self.__template_warehouses_data()

    def __template_warehouses_data(self) -> dict[str, any]:
        warehouse_input_path = self._get_warehouse_input_path()
        warehouse_output_path = self._get_warehouse_output_path()
        if not os.path.exists(warehouse_output_path):
            self._update_warehouse_file(warehouse_input_path, warehouse_output_path)
        return self.get_warehouses_data_mapped()

    @abstractmethod
    def _get_warehouse_input_path(self) -> str:
        pass

    @abstractmethod
    def _get_warehouse_output_path(self) -> str:
        pass

    @abstractmethod
    def get_warehouse_data(self, warehouse_id: str) -> dict[str, any]:
        pass

    @abstractmethod
    def get_warehouses_data(self) -> dict[str, any]:
        pass

    @abstractmethod
    def _update_warehouse_file(self, input_path: str, output_path: str) -> None:
        pass

    @abstractmethod
    def get_warehouses_data_mapped(self) -> dict[str, any]:
        pass

    @abstractmethod
    def get_warehouses_data_from_file(self, path: str) -> dict[str, any]:
        pass
