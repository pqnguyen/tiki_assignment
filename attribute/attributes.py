import datetime

from enums.enums import WeightUnit, StorageUnit
from exception.exceptions import *


class BaseAttribute:
    def __str__(self):
        return "Base attribute"


class Color(BaseAttribute):
    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return "Color: {color}".format(color=self.color)


class Storage(BaseAttribute):
    def __init__(self, value: int, unit: StorageUnit):
        if value <= 0:
            raise NegativeValueStorageException("Value of storage must be positive")

        self.value = value
        self.unit = unit

    def __str__(self):
        return "Storage: {value}{unit}".format(value=self.value, unit=self.unit.value)


class Description(BaseAttribute):
    def __init__(self, value: str = ""):
        self.value = value

    def __str__(self):
        return "Description: {description}".format(description=self.value)


class Origin(BaseAttribute):
    def __init__(self, value: str = ""):
        self.value = value

    def __str__(self):
        return "Origin: {origin}".format(origin=self.value)


class FactoryDate(BaseAttribute):
    def __init__(self, year: int, month: int, day: int):
        self.value = datetime.date(year, month, day)

    def __str__(self):
        return "Factory Date: {factory_date}".format(factory_date=self.value)


class Weight(BaseAttribute):
    def __init__(self, value: float, unit: WeightUnit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "Weight: {weight}{unit}".format(weight=self.value, unit=self.unit.value)


class Image(BaseAttribute):
    def __init__(self, src: str):
        self.src = src

    def __str__(self):
        return "Image src: {src}".format(src=self.src)