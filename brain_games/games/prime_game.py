import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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


def generate_question_and_answer():
    """Play a prime game with the user."""

    question = random.randint(1, 300)
    answer = 'yes' if is_prime(question) else 'no'

    return question, answer
