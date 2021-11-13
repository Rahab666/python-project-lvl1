import random


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


# Condition game
CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Logics game
def game():
    """Play a prime game with the user."""

    # Create random int and check prime
    chance_number = random.randint(1, 300)
    right_answer = check_prime(chance_number)

    return chance_number, right_answer
