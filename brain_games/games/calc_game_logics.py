import random
from brain_games.games import game_logics


# Create function for calculation random values
def random_expression(init_1, init_2, random_operator):
    """Accepts 2 random numbers, random operator(+,-,*).

    Return result calculation"""

    if random_operator == '+':
        return init_1 + init_2
    elif random_operator == '-':
        return init_1 - init_2
    elif random_operator == '*':
        return init_1 * init_2


# Logics game
def calc_game():
    """Play a calculate game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    # Condition game
    condition = 'What is the result of the expression?'

    # Greeting user
    hello_name = game_logics.welcome_user()
    print('{0} {1}\n{2}'.format(hello_name[0],
                                hello_name[1], condition))

    # Set by the counter value
    correct_answer = 0

    while correct_answer < 3:

        # Create random ints, operator and calculation expression
        operators = ('+-*')
        init_1 = random.randint(1, 100)
        init_2 = random.randint(1, 100)
        random_operator = random.choice(operators)
        chance_sample = '{} {} {}'.format(init_1, random_operator, init_2)
        right_answer = random_expression(init_1, init_2, random_operator)

        # Ask a Question
        game_logics.question(chance_sample)

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
