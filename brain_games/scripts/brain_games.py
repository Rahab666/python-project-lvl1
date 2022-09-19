#!/usr/bin/env python
"""Main script."""
import sys

from brain_games import cli
from brain_games.engine import start
from brain_games.exceptions import WrongAnswerError


def main():
    """Start brain games."""
    args = cli.parse()

    try:
        start(args.game)
    except WrongAnswerError:
        sys.exit(1)


if __name__ == '__main__':
    main()
