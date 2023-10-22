import ast
import json
import os
import pickle
from typing import Any

from jser.JserResolver.commission_resolver import JserCommissionResolver
from jser.constant import COMMISSION_WILDBERRIES_CSV, COMMISSION_KEY, COMMISSION_WILDBERRIES_BINARY, HandlerType, \
    RETURN_PERCENT_KEY


class WildberriesCommissionResolver(JserCommissionResolver):

    def __init__(self):
        super().__init__()

    def _get_commision_output_path(self):
        return COMMISSION_WILDBERRIES_BINARY

    def _get_commision_input_path(self):
        return COMMISSION_WILDBERRIES_CSV

    def _get_commission_for_niche(self, niche_name: str) -> dict[str, float]:
        if niche_name not in self._niche_commission_data:
            return {
                HandlerType.MARKETPLACE.value: 0,
                HandlerType.PARTIAL_CLIENT.value: 0,
                HandlerType.CLIENT.value: 0,
            }
        return self._niche_commission_data[niche_name]["commission"]

    def get_commission_for_niche_mapped(self, niche_name: str) -> dict:
        commission_for_niche: dict = self._get_commission_for_niche(niche_name)
        return {
            HandlerType.MARKETPLACE: commission_for_niche[
                HandlerType.MARKETPLACE.value
            ],
            HandlerType.PARTIAL_CLIENT: commission_for_niche[
                HandlerType.PARTIAL_CLIENT.value
            ],
            HandlerType.CLIENT: commission_for_niche[HandlerType.CLIENT.value],
        }

    def get_return_percent_for(self, niche_name: str) -> float:
        if niche_name not in self._niche_commission_data:
            return 0.0
        return self._niche_commission_data[niche_name][RETURN_PERCENT_KEY] / 100

    def update_niche_commission_file(self, input_path: str, output_path: str) -> None:
        with open(input_path, "r", encoding="cp1251") as file:
            if not os.path.exists('WildberriesOutput'):
                os.mkdir('WildberriesOutput')
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
            with open(output_path, 'ab') as out_file:
                pickle.dump(json_string, out_file)

    def get_commission_data(self, path) -> dict[str, Any]:
        with open(path, 'rb') as f:
            return ast.literal_eval(pickle.load(f))
