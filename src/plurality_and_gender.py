#*******************************************
# Joseph Winters
# Enums for describing plurality and gender
# Fall 2016
#*******************************************


import enum


@enum.unique
class Plurality(enum.Enum):
    """An enum to indicate if something is plural, or if that is unknown."""

    UNKNOWN  = 0
    SINGULAR = 1
    PLURAL   = 2


@enum.unique
class Gender(enum.Enum):
    """An enum to indicate if gender is masculine, feminine, or unknown."""

    UNKNOWN   = "x"
    MASCULINE = "m"
    FEMININE  = "f"
