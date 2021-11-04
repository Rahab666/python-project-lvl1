from random import randint
import prompt


def parity_check(a):
    """Check even and return yes or no"""
    if a % 2 == 0:
        return 'yes'
    return 'no'


def parity_game():
    """Play a parity game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    # Create short answer variables
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    wrong = 'is wrong answer ;(. Correct answer was'
    again = "Let's try again,"
    welcome = 'Welcome to the Brain Games!'
    r_u_name = 'May I have your name?'

    # Greeting user
    name = prompt.string('{0}\n{1} '.format(welcome, r_u_name))
    print('Hello, {0}\n{1}'.format(name, condition))

    # Create random int and check parity
    correct_answer = 0
    chance_number = randint(1, 100)
    check_even_chance_number = parity_check(chance_number)

    # Ask user the question
    print('Question: {0}'.format(chance_number))

    # User answer
    user_answer = prompt.string('Your answer: ')

    # If user write wrong answer
    if user_answer.casefold() != check_even_chance_number:
        return print("'{0}' {1} '{2}'.\n{3} {4}!".format(
            user_answer.casefold(), wrong,
            check_even_chance_number, again, name))

    # If user write correct answer
    while correct_answer < 2:
        print('Correct!')

        # Repeat for cycle
        chance_number = randint(1, 100)
        check_even_chance_number = parity_check(chance_number)

        print('Question: {0}'.format(chance_number))

        user_answer = prompt.string('Your answer: ')

        if user_answer.casefold() != check_even_chance_number:
            return print("'{0}' {1} '{2}'.\n{3} {4}!".format(
                user_answer.casefold(), wrong,
                check_even_chance_number, again, name))

        correct_answer += 1

    # User win
    return print('Congratulations, {0}!'.format(name))
