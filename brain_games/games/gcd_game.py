import random


# Create function for find gcd random numbers
def gcd_random_integers(integer_1, integer_2):
    """Accepts 2 random numbers, return gcd given numbers"""

    while integer_1 != 0 and integer_2 != 0:
        if integer_1 > integer_2:
            integer_1 = integer_1 % integer_2
        else:
            integer_2 = integer_2 % integer_1

    return integer_1 + integer_2


CONDITION = "Find the greatest common divisor of given numbers."


# Logics game
def game():
    """Play a gcd game with the user."""

    # Create random ints and find gcd ints
    random_integer_1 = random.randint(1, 100)
    random_integer_2 = random.randint(1, 100)
    right_answer = gcd_random_integers(random_integer_1, random_integer_2)
    chance_2_numbers = '{0} {1}'.format(random_integer_1, random_integer_2)

    return chance_2_numbers, right_answer
