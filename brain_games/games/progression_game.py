import random
from brain_games import game_logics


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

    while index_progression <= progression_length:
        if index_progression != random_number:
            result += '{0} '.format(progression[index_progression])
        elif index_progression == random_number:
            result += '{0} '.format('..')
        index_progression += 1

    return result


# Logics game
def progression_game():
    """Play a progression game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    condition = "What number is missing in the progression?"

    # Greeting user
    hello_name = game_logics.welcome_user()
    print('{0} {1}\n{2}'.format(hello_name[0],
                                hello_name[1], condition))

    # Set by the counter value
    correct_answer = 0

    while correct_answer < 3:

        # Create random progression and record progression in variable
        random_sequence = random_progression()

        # Choose member progression
        random_progression_number = random.randint(0, len(random_sequence) - 1)
        right_answer = random_sequence[random_progression_number]

        # Exclusion random member sequence and output result for user
        progression_for_user = exclusion_sequence_member(
            random_sequence, random_progression_number)

        # Ask a Question
        game_logics.question(progression_for_user)

        # User answer
        user_answer = game_logics.user_answer()

        # Comprasion of answers, if user answer - 'wrong', then end game
        right_or_wrong = game_logics.comparison_of_answers(
            user_answer, str(right_answer), hello_name[1])

        # If user answer right
        if right_or_wrong == 'Correct!':
            print(right_or_wrong)
            correct_answer += 1

        # If user answer wrong
        elif right_or_wrong != 'Correct!':
            return print(right_or_wrong)

    # User win
    return print('Congratulations, {0}!'.format(hello_name[1]))
