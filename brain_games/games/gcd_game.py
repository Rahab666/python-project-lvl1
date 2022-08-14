"""Logic of the gcd game."""
import random

import numpy

system_random = random.SystemRandom()

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    """Return question and answer for the gcd game."""
    first_number = system_random.randint(1, 100)
    second_number = system_random.randint(1, 100)

    answer = numpy.gcd(first_number, second_number)
    question = f'{first_number} {second_number}'

    return question, answer
