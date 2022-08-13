"""Engine for start games."""
import logging.config

import prompt
from brain_games.games import (calc_game, even_game, gcd_game, prime_game,
                               progression_game)
from brain_games.log_config import LOGGING_CONFIG, log_info

logging.config.dictConfig(LOGGING_CONFIG)

NUMBER_OF_ROUNDS: int = 3

GAMES = {
    'calc': calc_game,
    'even': even_game,
    'gcd': gcd_game,
    'prime': prime_game,
    'progression': progression_game,
}


def start(game):
    """Play a game with the user.

    If user answer right is 3 times, then user "win".
    If user answer wrong is 1 times, then user loos and game end.
    """
    game = GAMES.get(game.lower())

    log_info.info('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    log_info.info(f'Hello, {name}\n{game.DESCRIPTION}')

    for _ in range(NUMBER_OF_ROUNDS):

        question, right_answer = game.generate_question_and_answer()

        log_info.info(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if str(right_answer) == user_answer.casefold():
            log_info.info('Correct!')

        else:
            log_info.info("""'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!""".format(
                user_answer.casefold(), right_answer, name,
            ))
            return

    log_info.info(f'Congratulations, {name}!')
