class LexerException(Exception):
    """Unrecognized character."""

    def __init__(self, column, message):
        self.column = column
        self.message = message

class ParserException(Exception):
    """Unrecognized token sequence."""