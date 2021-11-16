#!/usr/bin/env python
from brain_games.games import even_game
from brain_games.engine import start


def main():
    """Start brain even game"""

    start(even_game)


if __name__ == '__main__':
    main()
