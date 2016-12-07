#******************************************
# Joseph Winters
# Enum for representing different subjects
# Fall 2016
#******************************************


import enum

import plurality_and_gender as pg


@enum.unique
class Subject(enum.Enum):
    """An enum to represent the different possible subjects."""

    JE    = "je"        # I
    TU    = "tu"        # informal singular you
    IL    = "il"        # he
    ELLE  = "elle"      # she
    ON    = "on"        # one, we
    NOUS  = "nous"      # we
    VOUS  = "vous"      # formal you, plural you
    ILS   = "ils"       # masculine they
    ELLES = "elles"     # feminine they


    @property
    def plurality(self):
        """Plurality: The plurality of self."""
        if self is Subject.VOUS:
            return pg.Plurality.UNKNOWN
        elif (self is Subject.NOUS) or (self is Subject.ILS) or \
             (self is Subject.ELLES):
            return pg.Plurality.PLURAL
        else:           # self is one of: JE, TU, IL, ELLE, ON
            return pg.Plurality.SINGULAR


    @property
    def gender(self):
        """Gender: The gender of self."""
        if (self is Subject.IL) or (self is Subject.ILS):
            return pg.Gender.MASCULINE
        elif (self is Subject.ELLE) or (self is Subject.ELLES):
            return pg.Gender.FEMININE
        else:           # self is one of: JE, TU, ON, NOUS, VOUS
            return pg.Gender.UNKNOWN
