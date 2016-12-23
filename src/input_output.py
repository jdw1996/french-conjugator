#**********************
# Joseph Winters
# Handle I/O functions
# Fall 2016
#**********************


import subject as sj


_WELCOME            = "Welcome to the French Conjugator!"
_GOOD_BYE           = "Good-bye!"

_ENTER_VERB         = "Enter the verb you would like to conjugate: "
_ENTER_SUBJECT      = ("Enter the subject you would like to conjugate for\n"
                       "(must be one of: je, tu, il, elle, on, nous, vous, "
                       "ils, elles): ")
_ENTER_IS_PLURAL    = "Should the subject be treated as plural? (y/n) "
_ENTER_IS_MASCULINE = "Should the subject be treated as masculine? (y/n) "

_CONJUGATION_IS     = "The conjugation of the verb is: "

_INVALID_VERB       = "I'm sorry, that is not a valid French verb."
_INVALID_SUBJECT    = "I'm sorry, that is not a valid French subject."
_INVALID_RESPONSE   = "I'm sorry, that is not a valid response."

_TRY_AGAIN          = "Would you like to conjugate another verb? (y/n) "


def welcome():
    """Print out a welcome message."""
    print(_WELCOME)


def get_verb():
    """Get a valid French verb from console input.

    Returns:
        A string ending in one of: "er", "ir", "re".
    """
    while True:
        verb_str = input(_ENTER_VERB)
        if _verb_is_valid(verb_str):
            return verb_str
        print(_INVALID_VERB)


def get_subject():
    """Get a valid French subject from console input.

    Returns:
        The Subject value the user wishes to conjugate for.
    """
    while True:
        subject_str = input(_ENTER_SUBJECT)
        if _subject_is_valid(subject_str):
            return subject_str
        print(_INVALID_SUBJECT)


def is_plural():
    """Decide whether the subject should be treated as plural or not.

    Returns:
        True if subject is plural; else False.
    """
    return _get_decision(_ENTER_IS_PLURAL)


def is_masculine():
    """Decide whether the subject should be treated as masculine or feminine.

    Returns:
        True if subject is masculine; else False.
    """
    return _get_decision(_ENTER_IS_MASCULINE)


def output_conjugated_phrase(conjugated_phrase):
    """Print out the conjugated phrase.

    Args:
        conjugated_phrase (str): The conjugated phrase to output.
    """
    print(_CONJUGATION_IS + conjugated_phrase)


def try_again():
    """Decide whether the user has another verb to conjugate.

    Returns:
        True if user wants to conjugate another verb; else False.
    """
    return _get_decision(_TRY_AGAIN)


def goodbye():
    """Print out a good-bye message."""
    print(_GOOD_BYE)


def _verb_is_valid(verb_str):
    """Return True if verb_str is a valid French verb; else False."""
    return (len(verb_str) >= 3) and (verb_str[-2:] in ["er", "ir", "re"])


def _subject_is_valid(subject_str):
    """Return True if subject_str is a valid French subject; else False."""
    try:
        subject = sj.Subject(subject_str)
        return True
    except:
        return False

def _get_decision(prompt):
    """Return True if the answer to the prompt is 'yes'; else False."""
    while True:
        response = input(prompt)
        if response in "Yy":
            return True
        elif response in "Nn":
            return False
        print(_INVALID_RESPONSE)
