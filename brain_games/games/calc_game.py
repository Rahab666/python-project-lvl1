import random

DESCRIPTION = 'What is the result of the expression?'


def calculate(number_1, number_2, operator):
    """Accepts 2 random numbers, random operator(+,-,*).

    Return result calculation"""

    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2


def generate_question_and_answer():
    """Play a calculate game with the user."""

    operators = ('+-*')
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    random_operator = random.choice(operators)
    question = f'{number_1} {random_operator} {number_2}'
    answer = calculate(number_1, number_2, random_operator)

    return question, answer
