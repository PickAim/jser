import os
import unittest
from os import listdir
from os.path import isfile, join

from jser.constant import COMMISSION_WILDBERRIES_CSV, WAREHOUSE_WILDBERRIES_JSON
from jser.niche.commission.Wildberries.wildberries_niche_commission_resolver import WildberriesCommissionResolver
from jser.warehouse.information.Wildberries.wildberries_warehouse_information_resolver import WildberriesDataResolver


class SerializeTest(unittest.TestCase):

    def test_update_niche_commission_file(self):
        object_jser_resolver = WildberriesCommissionResolver()
        object_jser_resolver.update_niche_commission_file(COMMISSION_WILDBERRIES_CSV, "test_niche_commission.pickle")
        onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        self.assertIn('test_niche_commission.pickle', onlyfiles)
        os.remove("test_niche_commission.pickle")

    def test_update_warehouse_file(self):
        object_jser_resolver = WildberriesDataResolver()
        object_jser_resolver.update_warehouse_file(WAREHOUSE_WILDBERRIES_JSON,
                                                   "test_warehouse_commission.pickle")
        onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        self.assertIn('test_warehouse_commission.pickle', onlyfiles)
        os.remove("test_warehouse_commission.pickle")
