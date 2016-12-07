#******************************************
# Joseph Winters
# Class for representing full conjugations
# Fall 2016
#******************************************


import enum

import plurality_and_gender as pg
import subject as sj


class Conjugation:
    """A class holding the full conjugation of a verb."""


    def __init__(self, infinitive, tense,
                 je_conj, tu_conj, il_elle_on_conj,
                 nous_conj, vous_conj, ils_elles_conj):
        """Create an instance of the Conjugation class.

        Args:
            infinitive (str): The infinitive of the verb the Conjugation is for.
            tense (Tense): The tense the verb is conjugated in.
            je_conj (str): The conjugation of the verb for "je", without the
                subject.
            tu_conj (str): The conjugation of the verb for "tu", without the
                subject.
            il_elle_on_conj (str): The conjugation of the verb for
                "il"/"elle"/"on", without the subject.
            nous_conj (str): The conjugation of the verb for "nous", without the
                subject.
            vous_conj (str): The conjugation of the verb for "vous", without the
                subject.
            ils_elles_conj (str): The conjugation of the verb for "ils"/"elles",
                without the subject.
        """
        self._infinitive = infinitive
        self._tense = tense
        je_form = "j'" if (je_conj[0] in "aeiouh") else "je "
        self._conjugations = \
            { sj.Subject.JE:    je_form + je_conj,
              sj.Subject.TU:    sj.Subject.TU.value + " " + tu_conj,
              sj.Subject.IL:    sj.Subject.IL.value + " " + il_elle_on_conj,
              sj.Subject.ELLE:  sj.Subject.ELLE.value + " " + il_elle_on_conj,
              sj.Subject.ON:    sj.Subject.ON.value + " " + il_elle_on_conj,
              sj.Subject.NOUS:  sj.Subject.NOUS.value + " " + nous_conj,
              sj.Subject.VOUS:  sj.Subject.VOUS.value + " " + vous_conj,
              sj.Subject.ILS:   sj.Subject.ILS.value + " " + ils_elles_conj,
              sj.Subject.ELLES: sj.Subject.ELLES.value + " " + ils_elles_conj }


    @property
    def infinitive(self):
        """str: The infinitive of the verb the Conjugation is for."""
        return self._infinitive


    @property
    def tense(self):
        """Tense: The tense the verb is conjugated in."""
        return self._tense


    def for_subject(self, subject):
        """Return the conjugation of the verb for subject.

        Args:
            subject (Subject): The subject to return the conjugation for.

        Returns:
            A string containing the requested conjugation, including the subject
            itself in the string.
        """
        return self._conjugations[subject]
