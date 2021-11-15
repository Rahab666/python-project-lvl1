import prompt


def logics(game):
    """Play a game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{game.DESCRIPTION}')

    RAUNDS = 3
    WRONG = 'is wrong answer ;(. Correct answer was'
    AGAIN = "Let's try again,"

    for correct_answer in range(RAUNDS):

        question, right_answer = game.generate_question_and_answer()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if str(right_answer) == user_answer.casefold():
            print('Correct!')

        else:
            return print(f"""'{user_answer.casefold()}' {WRONG} '{right_answer}'.
{AGAIN} {name}!""")

    print(f'Congratulations, {name}!')
