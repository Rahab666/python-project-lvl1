import random
from brain_games import game_logics


# Create function for find gcd random numbers
def gcd_random_integers(integer_1, integer_2):
    """Accepts 2 random numbers, return gcd given numbers"""

    while integer_1 != 0 and integer_2 != 0:
        if integer_1 > integer_2:
            integer_1 = integer_1 % integer_2
        else:
            integer_2 = integer_2 % integer_1

    return integer_1 + integer_2


# Logics game
def gcd_game():
    """Play a parity game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    condition = "Find the greatest common divisor of given numbers."

    # Greeting user
    hello_name = game_logics.welcome_user()
    print('{0} {1}\n{2}'.format(hello_name[0],
                                hello_name[1], condition))

    # Set by the counter value
    correct_answer = 0

    while correct_answer < 3:

        # Create random ints and find gcd ints
        random_integer_1 = random.randint(1, 100)
        random_integer_2 = random.randint(1, 100)
        right_answer = gcd_random_integers(random_integer_1, random_integer_2)
        chance_2_numbers = '{0} {1}'.format(random_integer_1, random_integer_2)

        # Ask a Question
        game_logics.question(chance_2_numbers)

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
