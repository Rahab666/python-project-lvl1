import prompt


def comparison_of_answers(user_answer, right_answer, name):
    """Accept username, user answer, right answer and comparison answers.

    If answers equally, return 'Correct!'"""

    WRONG = 'is wrong answer ;(. Correct answer was'
    AGAIN = "Let's try again,"

    if user_answer.casefold() != right_answer:
        return "'{0}' {1} '{2}'.\n{3} {4}!".format(
            user_answer.casefold(), WRONG,
            right_answer, AGAIN, name)

    return 'Correct!'


# Logics game
def logics(game):
    """Play a game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    # Greeting user
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('{0} {1}\n{2}'.format('Hello,',
                                name, game.CONDITION))

    # Set by the counter value
    correct_answer = 0
    RAUNDS = 3

    while correct_answer < RAUNDS:

        # Create random answer and question
        question, right_answer = game.game()

        # Ask a Question
        print('Question: {0}'.format(question))

        # User answer
        user_answer = prompt.string('Your answer: ')

        # Comprasion of answers, if user answer - 'wrong', then end game
        right_or_wrong = comparison_of_answers(
            user_answer, str(right_answer), name)

        # If user answer right
        if right_or_wrong == 'Correct!':
            print(right_or_wrong)
            correct_answer += 1

        # If user answer wrong
        elif right_or_wrong != 'Correct!':
            return print(right_or_wrong)

    # User win
    return print('Congratulations, {0}!'.format(name))
