#!/usr/bin/env python
"""Main script."""
from brain_games import cli
from brain_games.engine import start


def main():
    """Start brain games."""
    args = cli.parse()

    start(args.game)


if __name__ == '__main__':
    main()
