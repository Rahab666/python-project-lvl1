import random


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


# Condition game
CONDITION = 'What is the result of the expression?'


# Logics game
def game():
    """Play a calculate game with the user."""

    # Create random ints, operator and calculation expression
    operators = ('+-*')
    init_1 = random.randint(1, 100)
    init_2 = random.randint(1, 100)
    random_operator = random.choice(operators)
    chance_expression = f'{init_1} {random_operator} {init_2}'
    right_answer = random_expression(init_1, init_2, random_operator)

    return chance_expression, right_answer
