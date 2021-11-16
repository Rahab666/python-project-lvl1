#!/usr/bin/env python
from brain_games.games import gcd_game
from brain_games.engine import start


def main():
    """Start brain gcd game"""

    start(gcd_game)


if __name__ == '__main__':
    main()
