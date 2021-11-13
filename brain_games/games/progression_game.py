import random


# Create function for create random progression
def random_progression():
    """Create random progression of 10 numbers.

    Return tuple with 10 numbers sequence"""

    first_number_sequence = random.randint(1, 100)
    difference_btw_numbers = random.randint(1, 100)

    number_2 = first_number_sequence + difference_btw_numbers
    number_3 = number_2 + difference_btw_numbers
    number_4 = number_3 + difference_btw_numbers
    number_5 = number_4 + difference_btw_numbers
    number_6 = number_5 + difference_btw_numbers
    number_7 = number_6 + difference_btw_numbers
    number_8 = number_7 + difference_btw_numbers
    number_9 = number_8 + difference_btw_numbers
    number_10 = number_9 + difference_btw_numbers

    return (
        first_number_sequence, number_2, number_3, number_4, number_5,
        number_6, number_7, number_8, number_9, number_10)


# Create function for exlusion random member progression
def exclusion_sequence_member(progression, random_number):
    """Accepts progression and number progression.

    Return progression without number progression and replaces it '..'."""

    result = ''
    progression_length = len(progression) - 1
    index_progression = 0
    SKIP = '..'

    while index_progression <= progression_length:
        if index_progression != random_number:
            result += f'{progression[index_progression]} '
        elif index_progression == random_number:
            result += f'{SKIP} '
        index_progression += 1

    return result


CONDITION = "What number is missing in the progression?"


# Logics game
def game():
    """Play a progression game with the user."""

    # Create random progression and record progression in variable
    random_sequence = random_progression()

    # Exclusion of a member of the progression
    random_progression_number = random.randint(0, len(random_sequence) - 1)
    right_answer = random_sequence[random_progression_number]

    # Exclusion random member sequence and output result for user
    progression_for_user = exclusion_sequence_member(
        random_sequence, random_progression_number)

    return progression_for_user, right_answer
