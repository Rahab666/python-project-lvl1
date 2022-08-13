"""Parsing arguments from CLI."""

import argparse


def parse():  # pragma: no cover
    """Parse arguments from CLI.

    Return arguments as a string.
    """
    parser = argparse.ArgumentParser(
        description='description: the game that tests basic math knowledge.',
        prog='brain-games',
        usage='%(prog)s --game <game_name>',
    )

    parser.add_argument(
        '-V', '--version',
        version='%(prog)s 1.0',
        action='version',
        help='output the version number.',
    )

    parser.add_argument(
        '--game',
        help="""Available games:
        Gcd - сhecks knowledge of greatest common divisors. //
        Prime - сhecks knowledge of prime numbers. //
        Progression - сhecks knowledge of arithmetic progression. //
        Even - сhecks knowledge of even numbers. //
        Calc - сhecks knowledge of basic mathematical expressions. //""",
        metavar='[game]',
    )

    args = parser.parse_args()

    return args
