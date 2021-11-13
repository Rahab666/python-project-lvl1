from random import randint


# Create function for parity check integer
def parity_check(check_int):
    """Check even and return yes or no"""

    if check_int % 2 == 0:
        return 'yes'
    return 'no'


# Condition game
CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


# Logics game
def game():
    """Play a parity game with the user."""

    # Create random int and check parity
    chance_number = randint(1, 100)
    right_answer = parity_check(chance_number)

    return chance_number, right_answer
