import prompt


def start(game):
    """Play a game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{game.DESCRIPTION}')

    NUMBER_OF_ROUNDS = 3

    for correct_answer in range(NUMBER_OF_ROUNDS):

        question, right_answer = game.generate_question_and_answer()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if str(right_answer) == user_answer.casefold():
            print('Correct!')

        else:
            print("""'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!""".format(
                user_answer.casefold(), right_answer, name
            ))
            return

    print(f'Congratulations, {name}!')
