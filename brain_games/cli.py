import prompt
"""Simplify input and output."""


def welcome_user():
    """Return username input."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    return print(f'Hello, {name}')
