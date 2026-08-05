from cas.exceptions import LexerException
from cas.interpreter.token import Token, TokenType


class Lexer:
    """A scanner that tokenizes user input."""

    _SIMPLE_TOKENS = {"(": TokenType.L_PAREN, ")": TokenType.R_PAREN, ",": TokenType.COMMA, "=": TokenType.EQUALS, "+": TokenType.PLUS, "-": TokenType.MINUS, "*": TokenType.STAR, "/": TokenType.SLASH, "^": TokenType.CARAT}

    _KEYWORDS = {"let": TokenType.LET, "pi": TokenType.PI, "euler": TokenType.EULER}

    def __init__(self) -> None:
        # List of tokens
        self._tokens = []

        # Position indices
        self._start_of_lexeme = 0
        self._current = 0

    def tokenize(self, user_input) -> list[Token]:
        """Scan user input to create a list of tokens."""
        self._user_input = user_input
        while not self._isFinished():
            self._start_of_lexeme = self._current
            self._scanToken()
        return self._tokens

    def _scanToken(self) -> None:
        """Scan for an individual token."""
        char = self._advance()

        # Single character (or "simple") tokens
        if char in self._SIMPLE_TOKENS:
            self._addToken(self._SIMPLE_TOKENS[char])

        # Two character token
        elif char == ":":
            if self._peek() == "=":
                self._advance()
                self._addToken(TokenType.COLON_EQUALS)

        # Multi character tokens
        elif char.isalpha():
            self._getText()
        elif char.isdigit():
            self._getNumber()

        # Whitespace
        elif char in [" ", "\t"]:
            pass

        # Unrecognized token
        else:
            column = self._current + 1
            raise LexerException(column, f'Unrecognized character "{char}"!')

    def _getText(self) -> None:
        """Get text-based tokens, namely, identifiers and keywords."""
        while self._peek().isalnum() or self._peek() == "_":
            self._advance()

        text = self._user_input[self._start_of_lexeme : self._current]

        # Decide if text is a keyword or an identifier
        if text in self._KEYWORDS:
            type = self._KEYWORDS[text]
            self._addToken(type)
        else:
            self._addToken(TokenType.IDENTIFIER, text)

    def _getNumber(self) -> None:
        """Get number tokens."""
        while self._peek().isdigit() or (self._peek() == "." and self._nextPeek().isdigit()):
            self._advance()

        number = float(self._user_input[self._start_of_lexeme : self._current])
        self._addToken(TokenType.NUMBER, number)

    def _advance(self) -> str:
        """Read and return the current character, while advancing the index."""
        char = self._user_input[self._current]
        self._current += 1
        return char

    def _peek(self) -> str:
        """Read the next character from user input without advancing the index."""
        if self._isFinished():
            return "\0"
        # We can just look at _current because _advance() already pushes us by one index.
        return self._user_input[self._current]

    def _nextPeek(self) -> str:
        """Read the character after the next character without advancing the index."""
        if self._current + 1 >= len(self._user_input):
            return "\0"
        return self._user_input[self._current + 1]

    def _addToken(self, type: TokenType, value: object = None) -> None:
        """Add a token to the list of stored tokens."""
        text = self._user_input[self._start_of_lexeme : self._current]
        token = Token(type, text, value)
        self._tokens.append(token)

    def _isFinished(self) -> bool:
        """Check if lexing is complete."""
        return self._current >= len(self._user_input)


if __name__ == "__main__":
    pass
