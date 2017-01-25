#************************************************
# Joseph Winters
# Constants to hold conjugations of helper verbs
# Fall 2016
#************************************************


import conjugation as conj
import tense as tn


ALLER_PRESENT = conj.Conjugation("aller", tn.Tense.PRESENT,
                                 "vais", "vas", "va",
                                 "allons", "allez", "vont")
AVOIR_PRESENT = conj.Conjugation("avoir", tn.Tense.PRESENT,
                                 "ai", "as", "a", "avons", "avez", "ont")
ETRE_PRESENT = conj.Conjugation("être", tn.Tense.PRESENT,
                                "suis", "es", "est", "sommes", "êtes", "sont")

DR_MRS_VANDERTRAMPP_VERBS = {"devenir", "revenir", "monter", "rentrer",
                             "sortir", "venir", "arriver", "naître",
                             "descendre", "entrer", "retourner", "tomber",
                             "rester", "aller", "mourir", "passer", "partir"}
