import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def calculate_gcd(integer_1, integer_2):
    """Accepts 2 random numbers, return gcd given numbers"""

    while integer_1 != 0 and integer_2 != 0:
        if integer_1 > integer_2:
            integer_1 = integer_1 % integer_2
        else:
            integer_2 = integer_2 % integer_1

    return integer_1 + integer_2


def generate_question_and_answer():
    """Play a gcd game with the user."""

    random_integer_1 = random.randint(1, 100)
    random_integer_2 = random.randint(1, 100)
    answer = calculate_gcd(random_integer_1, random_integer_2)
    question = f'{random_integer_1} {random_integer_2}'

    return question, answer
