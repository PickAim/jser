import os
import unittest
from os import listdir
from os.path import isfile, join

from jser.niche.commission.serialize_niche_commission import update_niche_commission_file
from jser.warehouse.commision.serialize_warehouse_commision import update_warehouse_file


class SerializeTest(unittest.TestCase):
    def test_update_niche_commission_file(self):
        update_niche_commission_file("test_niche_commission.pickle")
        onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        self.assertIn('test_niche_commission.pickle', onlyfiles)
        os.remove("test_niche_commission.pickle")

    def test_update_warehouse_file(self):
        update_warehouse_file("test_warehouse_commission.pickle")
        onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
        self.assertIn('test_warehouse_commission.pickle', onlyfiles)
        os.remove("test_warehouse_commission.pickle")
