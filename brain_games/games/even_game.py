from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    """Play a parity game with the user."""

    chance_number = randint(1, 100)
    right_answer = 'no' if chance_number % 2 else 'yes'

    return chance_number, right_answer
