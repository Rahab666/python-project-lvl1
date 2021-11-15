import random


def is_prime(random_integer):
    """Check prime and return yes or no"""

    counter = 2

    if random_integer == 1:
        return False

    while counter < random_integer:
        if random_integer % counter != 0:
            counter += 1
        elif random_integer % counter == 0:
            return False
    return True


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    """Play a prime game with the user."""

    chance_number = random.randint(1, 300)
    right_answer = 'yes' if is_prime(chance_number) else 'no'

    return chance_number, right_answer
