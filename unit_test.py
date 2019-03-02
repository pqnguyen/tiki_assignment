import unittest

from app import app
from product.configurable_product import ConfigurableProduct


class TikiAssignment(unittest.TestCase):

    def test_create_iphone_64gb_black(self):
        iphoneX_64_black = app.create_iphoneX_64gb_black()
        self.assertTrue(iphoneX_64_black is not None)

    def test_create_iphone_128gb_yellow(self):
        iphoneX_128_yellow = app.create_iphoneX_128gb_yellow()
        self.assertTrue(iphoneX_128_yellow is not None)

    def test_create_configurable_product(self):
        iphoneX_64_black = app.create_iphoneX_64gb_black()
        iphoneX_128_yellow = app.create_iphoneX_128gb_yellow()

        self.assertTrue(iphoneX_64_black is not None)
        self.assertTrue(iphoneX_128_yellow is not None)
        iphoneX = ConfigurableProduct("Iphone X", iphoneX_64_black, iphoneX_128_yellow)

        self.assertTrue(iphoneX is not None)


if __name__ == '__main__':
    unittest.main()