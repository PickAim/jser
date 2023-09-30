import ast
import json
import pickle
from typing import Any

from jorm.market.infrastructure import HandlerType

from jser.constant import COMMISSION_WILDBERRIES_CSV, COMMISSION_KEY, COMMISSION_WILDBERRIES_BINARY


def update_niche_commission_file(output_path: str) -> None:
    with open(COMMISSION_WILDBERRIES_CSV, "r", encoding="cp1251") as file:
        commission_dict: dict = {}
        lines: list[str] = file.readlines()
        for line in lines:
            splitted: list[str] = line.split(";")
            commission_dict[splitted[1].lower()] = {
                COMMISSION_KEY: {
                    HandlerType.MARKETPLACE.value: float(splitted[2]) / 100,
                    HandlerType.PARTIAL_CLIENT.value: float(splitted[3]) / 100,
                    HandlerType.CLIENT.value: float(splitted[4]) / 100,
                }
            }
        json_string: str = json.dumps(commission_dict, indent=4, ensure_ascii=False)
        with open(output_path, 'wb') as out_file:
            pickle.dump(json_string, out_file)


def get_commission_data() -> dict[str, Any]:
    with open(COMMISSION_WILDBERRIES_BINARY, 'rb') as f:
        return ast.literal_eval(pickle.load(f))
