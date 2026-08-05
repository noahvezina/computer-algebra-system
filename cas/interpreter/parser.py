from cas.interpreter.lexer import Token, TokenType
from cas.interpreter.ast_nodes import Stmt, Decl, Expr, Add, Mult, Pow, Var
from cas.exceptions import ParserException

"""
stmt    :=  decl | expr
decl    :=  "let" ID ":=" expr
expr    :=  add
add     :=  mult { ( "+" | "-" ) mult }
mult    :=  pow { ( "*" | "/" ) pow }
pow     :=  unary [ "^" pow ]
unary   :=  [ "-" ] atom
atom    :=  call | NUMBER | ID | "(" expr ")" 
call    :=  ID "(" [ expr  { "," expr } ] ")"
"""


class Parser:

    _FUNCTIONS = ["sin", "cos", "tan", "sqrt"]
    _VARS = ["malaise"]

    def __init__(self, tokens) -> None:
        self._tokens = tokens
        self._current = 0

    def parse(self) -> Stmt:
        """Parse tokens into meaningful syntax trees."""
        if self._match(TokenType.LET):
            return self._decl()
        return self._expr()

    def _decl(self) -> Decl:
        """Get declaration statement."""
        name = self._consume(TokenType.IDENTIFIER)
        self._consume(TokenType.COLON_EQUALS)
        expr = self._expr()
        return Decl(name, expr)

    def _expr(self) -> Expr:
        """Get expression statement."""
        return self._add()

    def _add(self) -> Expr:
        """Get addition expression."""
        expr = self._mult()
        terms = []

        while self._match(TokenType.PLUS, TokenType.MINUS):
            if self._previous().type == TokenType.MINUS:
                terms.append(self._mult())  # Gotta figure out how to make this negative
            else:
                terms.append(self._mult())

        if terms:
            return Add(expr, *terms)
        return expr

    def _mult(self) -> Expr:
        """Get multiplication expression."""
        """
        3x^2 + xcos(3x) - 9(3x - 2)
        """

        

        expr = self._pow()

    def _pow(self) -> Expr:
        """Get power expression."""

    def _advance(self) -> Token:
        """Return the current token, while advancing the index."""
        if not self._isFinished:
            self._current += 1
        return self._previous()

    def _peek(self) -> Token:
        """Return the next token without advancing the index."""
        # We can just look at _current because _advance() already pushes us by one index.
        return self._tokens[self._current]

    def _match(self, types: list[TokenType]) -> bool:
        """Check if the next token is of any of the given types, advance token too."""
        for type in types:
            if self._check(type):
                self._advance()
                return True
        return False

    def _consume(self, type, message) -> Token:
        """Check and return the next token if it is of the given type, else throw an exception."""
        if self._check(type):
            return self._advance()
        column = self._current + 1
        raise ParserException(column, message)

    def _check(self, type: TokenType) -> bool:
        """Check if the next token is of the given type. Does not advance token."""
        if self._isFinished():
            return False
        return self._peek().type == type

    def _previous(self) -> Token:
        """Return the previous token."""
        return self._tokens[self.current - 1]

    def _isFinished(self) -> bool:
        """Check if parsing is complete."""
        return self._current >= len(self._tokens)
