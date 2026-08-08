class ComputerAlgebraSystemException(Exception):
    """A base class for custom exceptions."""

    def __init__(self, message: str, column: int = -1) -> None:
        self.message = message
        self.column = column


class LexerException(ComputerAlgebraSystemException):
    """Unrecognized character."""

    def __init__(self, message: str, column: int = -1) -> None:
        super().__init__(message, column)


class ParserException(ComputerAlgebraSystemException):
    """Unrecognized token sequence."""

    def __init__(self, message: str, column: int = -1) -> None:
        super().__init__(message, column)
