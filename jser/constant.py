import os
from enum import Enum
from pathlib import Path
from typing import Final

COMMISSION_KEY: Final[str] = "commission"
RETURN_PERCENT_KEY: Final[str] = "return_percent"

WILDBERRIES_NAME: Final[str] = 'wildberries'

file_dir: list[str] = os.path.dirname(os.path.abspath(__file__))


def get_path(dir_to_search: str, file_to_search: str):
    try:
        return str(next(Path(dir_to_search).rglob(file_to_search)))
    except StopIteration:
        return os.path.join(dir_to_search, file_to_search)


# __NICHE_TO_CATEGORY: Final[str] = get_path(file_dir, 'niche_to_category.paim')
# with open(__NICHE_TO_CATEGORY, 'rb') as file:
#     NICHE_TO_CATEGORY: Final[dict[str, str]] = pickle.load(file)

COMMISSION_WILDBERRIES_CSV: Final[str] = get_path(file_dir, 'niche_commission.csv')
COMMISSION_WILDBERRIES_BINARY: Final[str] = get_path(file_dir,
                                                     'niche_commission.pickle')
WAREHOUSE_WILDBERRIES_JSON: Final[str] = get_path(file_dir, 'data_warehouse.txt')
WAREHOUSE_WILDBERRIES_BINARY: Final[str] = get_path(file_dir, 'warehouse_data.pickle')

COMMISSION_KEY: Final[str] = "commission"
RETURN_PERCENT_KEY: Final[str] = "return_percent"


class HandlerType(Enum):
    MARKETPLACE = "market"
    PARTIAL_CLIENT = "partial client"
    CLIENT = "client"
