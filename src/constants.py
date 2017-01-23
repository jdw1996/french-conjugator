#***********************************
# Joseph Winters
# Useful constants for conjugations
# Winter 2017
#***********************************


import subject as sj


PRONOUNS = { sj.Subject.JE:    "me",
             sj.Subject.TU:    "te",
             sj.Subject.IL:    "se",
             sj.Subject.ELLE:  "se",
             sj.Subject.ON:    "se",
             sj.Subject.NOUS:  "nous",
             sj.Subject.VOUS:  "vous",
             sj.Subject.ILS:   "se",
             sj.Subject.ELLES: "se" }

IMPARFAIT_ENDINGS = { sj.Subject.JE:    "ais",
                      sj.Subject.TU:    "ais",
                      sj.Subject.IL:    "ait",
                      sj.Subject.ELLE:  "ait",
                      sj.Subject.ON:    "ait",
                      sj.Subject.NOUS:  "ions",
                      sj.Subject.VOUS:  "iez",
                      sj.Subject.ILS:   "aient",
                      sj.Subject.ELLES: "aient" }

PRESENT_ER_ENDINGS = { sj.Subject.JE:    "e",
                       sj.Subject.TU:    "es",
                       sj.Subject.IL:    "e",
                       sj.Subject.ELLE:  "e",
                       sj.Subject.ON:    "e",
                       sj.Subject.NOUS:  "ons",
                       sj.Subject.VOUS:  "ez",
                       sj.Subject.ILS:   "ent",
                       sj.Subject.ELLES: "ent" }

PRESENT_IR_ENDINGS = { sj.Subject.JE:    "is",
                       sj.Subject.TU:    "is",
                       sj.Subject.IL:    "it",
                       sj.Subject.ELLE:  "it",
                       sj.Subject.ON:    "it",
                       sj.Subject.NOUS:  "issons",
                       sj.Subject.VOUS:  "issez",
                       sj.Subject.ILS:   "issez",
                       sj.Subject.ELLES: "issez" }

PRESENT_RE_ENDINGS = { sj.Subject.JE:    "s",
                       sj.Subject.TU:    "s",
                       sj.Subject.IL:    "",
                       sj.Subject.ELLE:  "",
                       sj.Subject.ON:    "",
                       sj.Subject.NOUS:  "ons",
                       sj.Subject.VOUS:  "ez",
                       sj.Subject.ILS:   "ent",
                       sj.Subject.ELLES: "ent" }

FUTUR_SIMPLE_ENDINGS = { sj.Subject.JE:    "ai",
                         sj.Subject.TU:    "as",
                         sj.Subject.IL:    "a",
                         sj.Subject.ELLE:  "a",
                         sj.Subject.ON:    "a",
                         sj.Subject.NOUS:  "ons",
                         sj.Subject.VOUS:  "ez",
                         sj.Subject.ILS:   "ont",
                         sj.Subject.ELLES: "ont" }
