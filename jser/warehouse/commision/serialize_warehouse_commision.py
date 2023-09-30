import json
import pickle

from jser.constant import WAREHOUSE_WILDBERRIES_JSON, WAREHOUSE_WILDBERRIES_BINARY


def update_warehouse_file(output_path: str):
    with open(WAREHOUSE_WILDBERRIES_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)


def get_warehouse_data():
    with open(WAREHOUSE_WILDBERRIES_BINARY, 'rb') as f:
        return pickle.load(f)
