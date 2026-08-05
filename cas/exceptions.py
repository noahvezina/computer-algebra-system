class ComputerAlgebraSystemException(Exception):
    """A base class for custom exceptions."""

    def __init__(self, column: int, message: str) -> None:
        self.column = column
        self.message = message


class LexerException(ComputerAlgebraSystemException):
    """Unrecognized character."""

    def __init__(self, column: int, message: str) -> None:
        super().__init__(column, message)


class ParserException(ComputerAlgebraSystemException):
    """Unrecognized token sequence."""

    def __init__(self, column: int, message: str) -> None:
        super().__init__(column, message)
