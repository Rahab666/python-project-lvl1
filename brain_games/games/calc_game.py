"""Logic of the calculated game."""

import random

import numpy

system_random = random.SystemRandom()

DESCRIPTION = 'What is the result of the expression?'


def calculate(operator, *numbers):
    """Accept 2 random numbers and random operator(+,-,*).

    Return result calculation.
    """
    expressions = {
        '+': numpy.sum(list(numbers)),
        '-': numpy.subtract(*numbers),
        '*': numpy.multiply(*numbers),
    }

    return expressions.get(operator)


def generate_question_and_answer():
    """Return question and answer for the calculated game."""
    operators = '+-*'
    first_number = system_random.randint(1, 100)
    second_number = system_random.randint(1, 100)
    random_operator = system_random.choice(operators)

    answer = calculate(random_operator, first_number, second_number)
    question = f'{first_number} {random_operator} {second_number}'

    return question, answer
