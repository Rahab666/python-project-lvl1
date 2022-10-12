"""Custom exceptions for brain_games."""


class WrongAnswerError(Exception):
    """Raised if the answer is incorrect."""

    def __init__(self, game_name):
        """Initialize a name of the game for a class.

        Parameters
        ----------
        game_name : str
            The name of the game is where the exception is raised.

        """
        if game_name:
            self.message = f"User's answer is wrong for the {game_name} game"
        else:
            self.message = None

    def __str__(self):
        """Display error message.

        Returns
        -------
        result : str
            The text of the error.

        """
        if self.message:
            result = f'WrongAnswerException: {self.message} '
        else:
            result = 'WrongAnswerException has been raised'
        return result
