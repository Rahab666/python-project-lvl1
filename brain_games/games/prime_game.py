"""Logic of the prime game."""
import random

import sympy

system_random = random.SystemRandom()

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    """Return question and answer for the prime game."""
    number = system_random.randint(1, 300)

    answer = 'yes' if sympy.isprime(number) else 'no'
    question = number

    return question, answer
