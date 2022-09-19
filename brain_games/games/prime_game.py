"""Logic of the prime game."""
import random

import sympy

system_random = random.SystemRandom()

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    """Return question and answer for the prime game.

    Returns
    -------
    Union[str, str]
        Tuple containing:
            question : str
                One randomly generated int.
            answer : str
                If the int that is in question is prime,
                then 'yes', otherwise 'no'.

    """
    number = system_random.randint(1, 300)

    answer = 'yes' if sympy.isprime(number) else 'no'
    question = str(number)

    return question, answer
