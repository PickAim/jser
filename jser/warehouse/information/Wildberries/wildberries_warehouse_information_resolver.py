import json
import os
import pickle

from jser.JserResolver.information_resolver import JserInformationResolver
from jser.constant import WAREHOUSE_WILDBERRIES_JSON, WAREHOUSE_WILDBERRIES_BINARY


class WildberriesDataResolver(JserInformationResolver):

    def __init__(self):
        super().__init__()

    def _get_warehouse_output_path(self):
        return WAREHOUSE_WILDBERRIES_BINARY

    def _get_warehouse_input_path(self):
        return WAREHOUSE_WILDBERRIES_JSON

    def get_warehouses_data(self, path) -> dict[str, any]:
        path: str = self._get_warehouse_output_path()
        warehouses_data: dict[str, any] = self.get_warehouses_data_from_file(path)
        warehouse_dict: dict[int, any] = {}
        for data in warehouses_data['result']['resp']['data']:
            template_dict = {'name': data['warehouse'], 'address': data['address'], 'isFbs': data['isFbs'],
                             'isFbw': data['isFbw'], 'rating': data['rating']}
            warehouse_dict[data['id']] = template_dict
        return warehouse_dict

    def get_data_for_warehouse(self, id: int) -> dict[str, any]:
        mapping_warehouse: dict[str, any] = self.get_warehouses_data()
        return {id: mapping_warehouse[id]}

    def update_warehouse_file(self, input_path: str, output_path: str) -> None:
        with open(input_path, 'r', encoding='utf-8') as f:
            data: any = json.load(f)
        if not os.path.exists('WildberriesOutput'):
            os.mkdir('WildberriesOutput')
        with open(output_path, 'wb') as f:
            pickle.dump(data, f)

    def get_warehouses_data_from_file(self, path: str) -> dict[str, any]:
        with open(path, 'rb') as f:
            return pickle.load(f)
