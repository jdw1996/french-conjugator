#******************************************
# Joseph Winters
# Class for representing full conjugations
# Fall 2016
#******************************************


import enum

import constants as cn
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
        self._conjugations = \
            { sj.Subject.JE:    je_conj,
              sj.Subject.TU:    tu_conj,
              sj.Subject.IL:    il_elle_on_conj,
              sj.Subject.ELLE:  il_elle_on_conj,
              sj.Subject.ON:    il_elle_on_conj,
              sj.Subject.NOUS:  nous_conj,
              sj.Subject.VOUS:  vous_conj,
              sj.Subject.ILS:   ils_elles_conj,
              sj.Subject.ELLES: ils_elles_conj }


    @property
    def infinitive(self):
        """str: The infinitive of the verb the Conjugation is for."""
        return self._infinitive


    @property
    def tense(self):
        """Tense: The tense the verb is conjugated in."""
        return self._tense


    def for_subject(self, subject, pronominal=False):
        """Return the conjugation of the verb for subject.

        Args:
            subject (Subject): The subject to return the conjugation for.
            pronominal (boolean): True if the verb is pronominal.

        Returns:
            A string containing the requested conjugation, including the subject
            itself in the string.
        """
        subject_string = subject.value
        if pronominal:
            subject_string += " " + cn.PRONOUNS[subject]
        conjugated_verb = self._conjugations[subject]
        starts_with_vowel = conjugated_verb[0] in "aeéiouh"
        if starts_with_vowel and subject_string[-1] == "e":
            subject_string = subject_string[:-1] + "'"
        else:
            subject_string += " "
        return subject_string + conjugated_verb
