import random


DESCRIPTION = "What number is missing in the progression?"


def random_progression(first, difference, length):
    """Create random progression without one member.

    return skip number, result"""

    end = first + length * difference
    progression = range(first, end, difference)

    return progression


def generate_question_and_answer():
    """Play a progression game with the user."""

    first = random.randint(1, 100)
    difference = random.randint(1, 100)
    length = random.randint(5, 10)

    progression = random_progression(first, difference, length)

    question = ''
    progression_length = len(progression) - 1
    index_progression = 0
    hidden_number = random.randint(0, len(progression) - 1)
    answer = progression[hidden_number]

    while index_progression <= progression_length:
        if index_progression != hidden_number:
            question += f'{progression[index_progression]} '
        elif index_progression == hidden_number:
            question += '.. '
        index_progression += 1

    return question, answer
