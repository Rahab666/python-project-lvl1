"""Logic of the even game."""

import random

system_random = random.SystemRandom()

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    """Return question and answer for the even game.

    Returns
    -------
    Union[str, str]
        Tuple containing:
            question
                One randomly generated num.
            answer
                If the num that is in question is even,
                then 'yes', otherwise 'no'.

    """
    number = system_random.randint(1, 100)

    answer = 'no' if number % 2 else 'yes'
    question = str(number)

    return question, answer
