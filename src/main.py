#!/usr/bin/env python3

#****************
# Joseph Winters
# Main execution
# Fall 2016
#****************


from input_output import *
from irregular_verbs import *
from subject import *
from verb import *


def main():
    welcome()
    while True:
        verb_str = get_verb()
        verb = IRREGULAR_VERBS.get(verb_str)
        if verb is None:
            verb = Verb(verb_str)
        subject_str = get_subject()
        subject = Subject(subject_str)
        tense = get_tense()
        conjugation = verb.conjugate(subject, tense)
        output_conjugated_phrase(conjugation)
        if not try_again():
            break
    goodbye()


if __name__ == "__main__":
    main()
