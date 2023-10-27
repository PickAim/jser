import json
import pickle

from jser.JserResolver.commission_resolver import CommissionResolver
from jser.constant import COMMISSION_WILDBERRIES_CSV, COMMISSION_WILDBERRIES_BINARY, HandlerType, \
    RETURN_PERCENT_KEY


class WildberriesCommissionResolver(CommissionResolver):

    def __init__(self):
        super().__init__()

    def _get_commission_output_path(self) -> str:
        return COMMISSION_WILDBERRIES_BINARY

    def _get_commission_input_path(self) -> str:
        return COMMISSION_WILDBERRIES_CSV

    def _get_commission_for_niche(self, niche_name: str) -> dict[str, float]:
        # print(self._niche_commission_data)
        if niche_name not in self._niche_commission_data:
            return {
                HandlerType.MARKETPLACE.value: 0,
                HandlerType.PARTIAL_CLIENT.value: 0,
                HandlerType.CLIENT.value: 0,
            }
        return self._niche_commission_data[niche_name]["commission"]

    def get_commission_for_niche_mapped(self, niche_name: str) -> dict:
        commission_for_niche: dict = self._get_commission_for_niche(niche_name)
        # print(commission_for_niche)
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
            json_data = json.load(file)
            with open(output_path, 'wb+') as out_file:
                pickle.dump(json_data, out_file)

    def get_commission_data(self, path) -> dict[str, any]:
        with open(path, 'rb') as f:
            return pickle.load(f)
