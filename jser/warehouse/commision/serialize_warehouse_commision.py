import json
import pickle

from jser.constant import WAREHOUSE_WILDBERRIES_JSON


def update_warehouse_file(output_path: str):
    with open(WAREHOUSE_WILDBERRIES_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)
