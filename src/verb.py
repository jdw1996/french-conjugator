#******************************
# Joseph Winters
# Class for representing verbs
# Fall 2016
#******************************


import constants as cn
import helper_verbs as hv
import plurality_and_gender as pg
import subject as sj
import tense as tn


class Verb:
    """A class representing a verb."""


    def __init__(self, infinitive, **kwargs):
        """Create an instance of the Verb class.

        Args:
            infinitive (str): The infinitive of the verb.
            **kwargs:
                participe_passe (str): The participe passé for the verb.
                futur_simple_stem (str): The stem (ending in "r") used for
                    conjugation in futur simple.
                passe_compose_conjugation (Conjugation): The full conjugation of
                    the verb in passé composé.
                imparfait_conjugation (Conjugation): The full conjugation of the
                    verb in imparfait.
                present_conjugation (Conjugation): The full conjugation of the
                    verb in present tense.
                futur_proche_conjugation (Conjugation): The full conjugation of
                    the verb in futur proche.
                futur_simple_conjugation (Conjugation): The full conjugation of
                    the verb in futur simple.

        """
        if infinitive[:3] == "se ":
            self._pronominal = True
            self._infinitive = infinitive[3:]
        elif infinitive[:2] == "s'":
            self._pronominal = True
            self._infinitive = infinitive[2:]
        else:
            self._pronominal = False
            self._infinitive = infinitive
        self._ending = self._infinitive[-2:]
        self._without_ending = self._infinitive[:-2]
        self._participe_passe = kwargs.get("participe_passe")
        self._futur_simple_stem = kwargs.get("futur_simple_stem")
        self._passe_compose_conjugation = \
            kwargs.get("passe_compose_conjugation")
        self._imparfait_conjugation = kwargs.get("imparfait_conjugation")
        self._present_conjugation = kwargs.get("present_conjugation")
        self._futur_proche_conjugation = kwargs.get("futur_proche_conjugation")
        self._futur_simple_conjugation = kwargs.get("futur_simple_conjugation")


    @property
    def infinitive(self):
        """str: The infinitive of the verb."""
        return self._infinitive


    def conjugate(self, subject, tense):
        """Return the conjugation of the verb for subject and tense.

        Args:
            subject (Subject): The subject to conjugate the verb for.
            tense (Tense): The tense to conjugate the verb in.

        Returns:
            A string containing the requested conjugation, including the subject
            itself in the string.
        """
        if tense is tn.Tense.PASSE_COMPOSE:
            return self._conjugate_passe_compose(subject)
        elif tense is tn.Tense.IMPARFAIT:
            return self._conjugate_imparfait(subject)
        elif tense is tn.Tense.PRESENT:
            return self._conjugate_present(subject)
        elif tense is tn.Tense.FUTUR_PROCHE:
            return self._conjugate_futur_proche(subject)
        else:           # must be tn.Tense.FUTUR_SIMPLE
            return self._conjugate_futur_simple(subject)


    def _conjugate_passe_compose(self, subject):
        """Return the conjugation of the verb in passé composé with subject."""
        if self._passe_compose_conjugation is not None:
            return self._passe_compose_conjugation.for_subject(subject)

        if self._participe_passe is not None:
            participe_passe = self._participe_passe
        elif self._ending == "er":
            participe_passe = self._without_ending + "é"
        elif self._ending == "ir":
            participe_passe = self._without_ending + "i"
        else:           # must be "re"
            participe_passe = self._without_ending + "u"

        if (self._infinitive in hv.DR_MRS_VANDERTRAMPP_VERBS) \
            or self._pronominal:
            agreement = ""
            if subject.gender is pg.Gender.FEMININE:
                agreement += "e"
            if subject.plurality is pg.Plurality.PLURAL:
                agreement += "s"
            return hv.ETRE_PRESENT.for_subject(subject, self._pronominal) \
                   + " " + participe_passe + agreement
        else:
            return hv.AVOIR_PRESENT.for_subject(subject) + " " + participe_passe


    def _conjugate_imparfait(self, subject):
        """Return the conjugation of the verb in imparfait with subject."""
        if self._imparfait_conjugation is not None:
            return self._imparfait_conjugation.for_subject(subject)

        if self.infinitive == "être":
            stem = "ét"
        else:
            stem = self._conjugate_present(sj.Subject.NOUS).split()[-1][:-3]
        if (subject is not sj.Subject.NOUS) and \
           (subject is not sj.Subject.VOUS):
            if stem[-1] == "g":
                stem += "e"
            if stem[-1] == "c":
                stem = stem[:-1] + "ç"

        subject_string = subject.value
        if self._pronominal:
            subject_string += " " + cn.PRONOUNS[subject]
        starts_with_vowel = stem[0] in "aeéiouh"
        if starts_with_vowel and subject_string[-1] == "e":
            subject_string = subject_string[:-1] + "'"
        else:
            subject_string += " "

        all_but_ending = subject_string + stem

        if subject is sj.Subject.JE:
            return all_but_ending + "ais"
        elif subject is sj.Subject.TU:
            return all_but_ending + "ais"
        elif (subject is sj.Subject.IL) or (subject is sj.Subject.ELLE) or \
             (subject is sj.Subject.ON):
            return all_but_ending + "ait"
        elif subject is sj.Subject.NOUS:
            return all_but_ending + "ions"
        elif subject is sj.Subject.VOUS:
            return all_but_ending + "iez"
        else:       # must be one of: sj.Subject.ILS, sj.Subject.ELLES
            return all_but_ending + "aient"


    def _conjugate_present(self, subject):
        """Return the conjugation of the verb in présent with subject."""
        if self._present_conjugation is not None:
            return self._present_conjugation.for_subject(subject)

        subject_string = subject.value
        if self._pronominal:
            subject_string += " " + cn.PRONOUNS[subject]
        starts_with_vowel = self._without_ending[0] in "aeéiouh"
        if starts_with_vowel and subject_string[-1] == "e":
            subject_string = subject_string[:-1] + "'"
        else:
            subject_string += " "

        all_but_ending = subject_string + self._without_ending

        if self._ending == "er":
            if subject is sj.Subject.JE:
                return all_but_ending + "e"
            elif subject is sj.Subject.TU:
                return all_but_ending + "es"
            elif (subject is sj.Subject.IL) or (subject is sj.Subject.ELLE) or \
                 (subject is sj.Subject.ON):
                return all_but_ending + "e"
            elif subject is sj.Subject.NOUS:
                return all_but_ending + "ons"
            elif subject is sj.Subject.VOUS:
                return all_but_ending + "ez"
            else:       # must be one of: sj.Subject.ILS, sj.Subject.ELLES
                return all_but_ending + "ent"

        elif self._ending == "ir":
            if subject is sj.Subject.JE:
                return all_but_ending + "is"
            elif subject is sj.Subject.TU:
                return all_but_ending + "is"
            elif (subject is sj.Subject.IL) or (subject is sj.Subject.ELLE) or \
                 (subject is sj.Subject.ON):
                return all_but_ending + "it"
            elif subject is sj.Subject.NOUS:
                return all_but_ending + "issons"
            elif subject is sj.Subject.VOUS:
                return all_but_ending + "issez"
            else:       # must be one of: sj.Subject.ILS, sj.Subject.ELLES
                return all_but_ending + "issent"

        else:           # must be "re"
            if subject is sj.Subject.JE:
                return all_but_ending + "s"
            elif subject is sj.Subject.TU:
                return all_but_ending + "s"
            elif (subject is sj.Subject.IL) or (subject is sj.Subject.ELLE) or \
                 (subject is sj.Subject.ON):
                return all_but_ending
            elif subject is sj.Subject.NOUS:
                return all_but_ending + "ons"
            elif subject is sj.Subject.VOUS:
                return all_but_ending + "ez"
            else:       # must be one of: sj.Subject.ILS, sj.Subject.ELLES
                return all_but_ending + "ent"


    def _conjugate_futur_proche(self, subject):
        """Return the conjugation of the verb in futur proche with subject."""
        if self._futur_proche_conjugation is not None:
            return self._futur_proche_conjugation.for_subject(subject)
        return hv.ALLER_PRESENT.for_subject(subject) + " " + \
               cn.PRONOUNS[subject] + " " + self._infinitive


    def _conjugate_futur_simple(self, subject):
        """Return the conjugation of the verb in futur simple with subject."""
        if self._futur_simple_conjugation is not None:
            return self._futur_simple_conjugation.for_subject(subject)

        if self._futur_simple_stem is None:
            if self._ending == "re":
                stem = self._infinitive[:-1]
            else:
                stem = self._infinitive
        else:
            stem = self._futur_simple_stem

        subject_string = subject.value
        if self._pronominal:
            subject_string += " " + cn.PRONOUNS[subject]
        starts_with_vowel = stem[0] in "aeéiouh"
        if starts_with_vowel and subject_string[-1] == "e":
            subject_string = subject_string[:-1] + "'"
        else:
            subject_string += " "

        all_but_ending = subject_string + stem

        if subject is sj.Subject.JE:
            return all_but_ending + "ai"
        elif subject is sj.Subject.TU:
            return all_but_ending + "as"
        elif (subject is sj.Subject.IL) or (subject is sj.Subject.ELLE) or \
             (subject is sj.Subject.ON):
            return all_but_ending + "a"
        elif subject is sj.Subject.NOUS:
            return all_but_ending + "ons"
        elif subject is sj.Subject.VOUS:
            return all_but_ending + "ez"
        else:       # must be one of: sj.Subject.ILS, sj.Subject.ELLES
            return all_but_ending + "ont"
