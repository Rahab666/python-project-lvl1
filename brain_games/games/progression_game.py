import random


def random_progression():
    """Create random progression without one member.

    return skip number, result"""

    first = random.randint(1, 100)
    difference = random.randint(1, 100)
    length = random.randint(5, 10)
    end = first + length * difference
    progression = range(first, end, difference)

    result = ''
    progression_length = len(progression) - 1
    index_progression = 0
    SKIP = '..'
    hidden_number = random.randint(0, len(progression) - 1)
    skip_number = progression[hidden_number]

    while index_progression <= progression_length:
        if index_progression != hidden_number:
            result += f'{progression[index_progression]} '
        elif index_progression == hidden_number:
            result += f'{SKIP} '
        index_progression += 1

    return skip_number, result


DESCRIPTION = "What number is missing in the progression?"


def generate_question_and_answer():
    """Play a progression game with the user."""

    right_answer, result = random_progression()

    return result, right_answer
