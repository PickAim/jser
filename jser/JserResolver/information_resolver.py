import os
from abc import ABC, abstractmethod


class JserInformationResolver(ABC):
    def __init__(self):
        self._warehouse_data: dict = self.__template_warehouses_data()

    def __template_warehouses_data(self) -> dict[str, any]:
        warehouse_input_path = self._get_warehouse_input_path()
        warehouse_output_path = self._get_warehouse_output_path()
        if not os.path.exists(warehouse_output_path):
            self.update_warehouse_file(warehouse_input_path, warehouse_output_path)
        return self.get_warehouses_data(warehouse_output_path)

    @abstractmethod
    def _get_warehouse_input_path(self) -> str:
        pass

    @abstractmethod
    def _get_warehouse_output_path(self) -> str:
        pass

    @abstractmethod
    def get_data_for_warehouse(self, warehouse_id: str) -> dict[str, any]:
        pass

    @abstractmethod
    def update_warehouse_file(self, input_path: str, output_path: str) -> None:
        pass

    @abstractmethod
    def get_warehouses_data(self, path: str) -> dict[str, any]:
        pass

    @abstractmethod
    def get_warehouses_data_from_file(self, path: str) -> dict[str, any]:
        pass
