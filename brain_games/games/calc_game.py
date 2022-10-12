"""Logic of the calculated game."""

import random

import numpy

system_random = random.SystemRandom()

DESCRIPTION = 'What is the result of the expression?'


def calculate(operator, *numbers):
    """Accept 2 random numbers and random operator(+,-,*).

    Parameters
    ----------
    operator : str
        The operator to perform an arithmetic operation.
        It can be '+', '-' or '*'.
    numbers : int
        Numbers with which to perform an arithmetic operation.

    Returns
    -------
    result : int
        The result of an arithmetic operation.

    """
    expressions = {
        '+': numpy.sum(list(numbers)),
        '-': numpy.subtract(*numbers),
        '*': numpy.multiply(*numbers),
    }

    result = expressions.get(operator)

    return result


def generate_question_and_answer():
    """Return question and answer for the calculated game.

    Returns
    -------
    Union[str, str]
        Tuple containing:
            question
                A random arithmetic expression with two nums and one operator.
            answer
                The num that is missing in the arithmetic progression.

    """
    operators = '+-*'
    first_number = system_random.randint(1, 100)
    second_number = system_random.randint(1, 100)
    random_operator = system_random.choice(operators)

    answer = str(calculate(random_operator, first_number, second_number))
    question = f'{first_number} {random_operator} {second_number}'

    return question, answer
