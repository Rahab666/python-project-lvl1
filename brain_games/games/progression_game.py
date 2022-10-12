"""Logic of the progression game."""

import random

system_random = random.SystemRandom()

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    """Return question and answer for the progression game.

    Returns
    -------
    Union[str, str]
        Tuple containing:
            question
                One random arithmetic progression with one missing num.
            answer
                The num that is missing in the arithmetic progression.

    """
    first = system_random.randint(1, 100)
    difference = system_random.randint(1, 100)
    length = system_random.randint(5, 10)
    end = first + length * difference

    progression = range(first, end, difference)

    question = ''
    progression_length = len(progression) - 1
    index_progression = 0
    hidden_number = system_random.randint(0, len(progression) - 1)
    answer = str(progression[hidden_number])

    for index_progression in range(progression_length):
        if index_progression == hidden_number:
            question += '.. '
        else:
            question += f'{progression[index_progression]} '

    return question, answer
