#!/usr/bin/env python
from brain_games.games import prime_game
from brain_games.engine import start


def main():
    """Start brain prime game"""

    start(prime_game)


if __name__ == '__main__':
    main()
