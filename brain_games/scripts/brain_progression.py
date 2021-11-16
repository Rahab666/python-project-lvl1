#!/usr/bin/env python
from brain_games.games import progression_game
from brain_games.engine import start


def main():
    """Start brain progression game"""

    start(progression_game)


if __name__ == '__main__':
    main()
