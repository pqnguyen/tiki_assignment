from collections import OrderedDict

from enums.enums import Currency
from attribute.attributes import *


class Product:
    def __init__(self, name: str, sale_price: float, market_price: float, unit_price: Currency):
        self.validate_data(name, sale_price, market_price)

        self.name = name
        self.sale_price = sale_price
        self.market_price = market_price
        self.unit_price = unit_price
        self.attributes = []
        self.images = OrderedDict()
        self.default_image = None

    # this function is used to validate data before initialize product
    def validate_data(self, name: str, sale_price: float, market_price: float):
        if sale_price <= 0 or market_price <= 0:
            raise NegativePriceException("Price must be positive")

    def add_attribute(self, attribute: BaseAttribute):
        self.attributes.append(attribute)

    def add_attributes(self, attributes: list):
        self.attributes.extend(attributes)

    def add_image(self, image: Image):
        self.images[image] = image

    def set_default_image(self, image: Image):
        if image not in self.images:
            self.add_image(image)

        self.default_image = image

    def __str__(self):
        print("name: {name}\nSale Price: {unit}{sale_price}\nMarket Price: {unit}{market_price}".format(
            unit=self.unit_price.value, name=self.name, sale_price=self.sale_price, market_price=self.market_price
        ))

        for attribute in self.attributes:
            print(attribute)

        for image in self.images:
            print(image)

        print("Default image src:", self.default_image.src)

        return ""
