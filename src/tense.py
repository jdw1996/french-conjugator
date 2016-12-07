#*********************************************
# Joseph Winters
# Enum for representing different verb tenses
# Fall 2016
#*********************************************


import enum


@enum.unique
class Tense(enum.Enum):
    """An enum to represent different verb tenses."""

    PASSE_COMPOSE = "passé composé"
    IMPARFAIT     = "imparfait"
    PRESENT       = "présent"
    FUTUR_PROCHE  = "futur proche"
    FUTUR_SIMPLE  = "futur simple"
