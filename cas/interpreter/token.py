from enum import Enum, auto

class TokenType(Enum):
    """A collection of the different types of tokens."""

    # Literals
    IDENTIFIER = auto()
    NUMBER = auto()

    # Keywords
    LET = auto()

    # Constants
    PI = auto()
    EULER = auto()

    # Delimiters
    L_PAREN = auto()
    R_PAREN = auto()
    COMMA = auto()

    # Operators
    COLON_EQUALS = auto()
    EQUALS = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    CARAT = auto()

    # Invisible operator
    IMPLICIT = auto()


class Token:
    """A representation of an individual token."""

    def __init__(self, type: TokenType, text: str) -> None:
        self.type = type
        self.text = text

    def __repr__(self) -> str:
        if self.type in [TokenType.IDENTIFIER, TokenType.NUMBER]:
            return f"({self.type.name}: {self.text})"
        return f"({self.type.name})"