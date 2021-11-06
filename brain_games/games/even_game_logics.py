from random import randint
from brain_games.games import game_logics


# Create function for parity check integer
def parity_check(check_int):
    """Check even and return yes or no"""

    if check_int % 2 == 0:
        return 'yes'
    return 'no'


# Logics game
def parity_game():
    """Play a parity game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    # Condition game
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'

    # Greeting user
    hello_name = game_logics.welcome_user()
    print('{0} {1}\n{2}'.format(hello_name[0],
                                hello_name[1], condition))

    # Set by the counter value
    correct_answer = 0

    while correct_answer < 3:

        # Create random int and check parity
        chance_number = randint(1, 100)
        right_answer = parity_check(chance_number)

        # Ask a Question
        game_logics.question(chance_number)

        # User answer
        user_answer = game_logics.user_answer()

        # Comprasion of answers, if user answer - 'wrong', then end game
        right_or_wrong = game_logics.comparison_of_answers(
            user_answer, right_answer, hello_name[1])

        # If user answer right
        if right_or_wrong == 'Correct!':
            print(right_or_wrong)
            correct_answer += 1

        # If user answer wrong
        elif right_or_wrong != 'Correct!':
            return print(right_or_wrong)

    # User win
    return print('Congratulations, {0}!'.format(hello_name[1]))
