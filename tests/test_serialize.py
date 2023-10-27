import unittest

from jser.niche.commission.Wildberries.wildberries_niche_commission_resolver import WildberriesCommissionResolver
from jser.warehouse.information.Wildberries.wildberries_warehouse_information_resolver import \
    WildberriesInformationResolver


class SerializeTest(unittest.TestCase):

    def test_update_niche_commission_file(self):
        object_jser_resolver = WildberriesCommissionResolver()
        niche_commission = object_jser_resolver.get_commission_for_niche_mapped('Кофе зерновой')
        self.assertNotEqual(0, len(niche_commission))
        niche_percent = object_jser_resolver.get_return_percent_for('Кофе зерновой')
        self.assertNotEqual(0, niche_percent)

    def test_get_warehouse__data_from_file(self):
        object_jser_resolver = WildberriesInformationResolver()
        warehouses_data = object_jser_resolver.get_warehouses_data()
        self.assertNotEqual(0, len(warehouses_data))
