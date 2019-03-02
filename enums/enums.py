from enum import Enum


class WeightUnit(Enum):
    G = "gram"
    Kg = "Kg"


class StorageUnit(Enum):
    Byte = "B"
    Kb = "Kb"
    Gb = "Gb"


class Colour(Enum):
    Black = "Black"
    Yellow = "Yellow"


class Currency(Enum):
    VND = "VND"
    Dollar = "$"
