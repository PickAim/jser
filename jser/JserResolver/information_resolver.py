import os
from abc import ABC, abstractmethod

from jser.constant import WAREHOUSE_WILDBERRIES_BINARY
from jser.warehouse.information.serialize_warehouse_information import get_warehouses_data, update_warehouse_file


class JserInformationResolver(ABC):
    def __init__(self):
        self._warehouse_data: dict = self.__template_get_warehouses_data()

    def __template_get_warehouses_data(self) -> dict[str, any]:
        if not os.path.exists(WAREHOUSE_WILDBERRIES_BINARY):
            update_warehouse_file(WAREHOUSE_WILDBERRIES_BINARY)
        return get_warehouses_data()

    @abstractmethod
    def get_data_for_warehouse(self, warehouse_id: str) -> float:
        pass
