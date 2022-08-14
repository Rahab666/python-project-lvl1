"""Custom exceptions for brain_games."""


class WrongAnswerException(Exception):
    """Raised if the answer is incorrect."""

    def __init__(self, game_name):
        """Initialize a name of the game for a class."""
        if game_name:
            self.message = f"User's answer is wrong for the {game_name} game"
        else:
            self.message = None

    def __str__(self):
        """Display error message."""
        if self.message:
            return f'WrongAnswerException: {self.message} '
        else:
            return 'WrongAnswerException has been raised'
