"""Logic of the even game."""

import random

system_random = random.SystemRandom()

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    """Return question and answer for the even game."""
    number = system_random.randint(1, 100)

    answer = 'no' if number % 2 else 'yes'
    question = number

    return question, answer
