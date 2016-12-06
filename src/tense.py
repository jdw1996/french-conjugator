#*********************************************
# Joseph Winters
# Enum for representing different verb tenses
# Fall 2016
#*********************************************


import enum


@enum.unique
class Tense(enum.Enum):
    PC = "passé composé"
    IM = "imparfait"
    PR = "présent"
    FP = "futur proche"
    FS = "futur simple"
