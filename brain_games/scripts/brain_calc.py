#!/usr/bin/env python
from brain_games.games import calc_game
from brain_games.game_logics import logics


def main():
    """Start brain even game"""

    logics(calc_game)


if __name__ == '__main__':
    main()
