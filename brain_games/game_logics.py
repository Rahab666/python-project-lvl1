import prompt


wrong = 'is wrong answer ;(. Correct answer was'
again = "Let's try again,"


def welcome_user():
    """Return tuple ('Hello', username input)."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return ('Hello,', name)


def question(what_ask):
    '''Takes an argument and asks a question'''

    return print('Question: {0}'.format(what_ask))


def user_answer():
    '''Input user answer'''

    return prompt.string('Your answer: ')


def comparison_of_answers(user_answer, right_answer, name):
    """Accept username, user answer, right answer and comparison answers.

    If answers equally, return 'Correct!'"""

    if user_answer.casefold() != right_answer:
        return "'{0}' {1} '{2}'.\n{3} {4}!".format(
            user_answer.casefold(), wrong,
            right_answer, again, name)

    return 'Correct!'
