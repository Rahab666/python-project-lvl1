import random
from brain_games import game_logics


# Create function for prime check integer
def check_prime(random_integer):
    """Check prime and return yes or no"""

    counter = 2

    if random_integer == 1:
        return 'no'

    while counter < random_integer:
        if random_integer % counter != 0:
            counter += 1
        elif random_integer % counter == 0:
            return 'no'
    return 'yes'


# Logics game
def prime_game():
    """Play a prime game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    # Condition game
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    # Greeting user
    hello_name = game_logics.welcome_user()
    print('{0} {1}\n{2}'.format(hello_name[0],
                                hello_name[1], condition))

    # Set by the counter value
    correct_answer = 0

    while correct_answer < 3:

        # Create random int and check prime
        chance_number = random.randint(1, 300)
        right_answer = check_prime(chance_number)

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
