from cas.interpreter.token import Token, TokenType
from cas.interpreter.ast_nodes import Stmt, Decl, Expr, Add, Mult, Pow, Call, Var, Num, Float, Rational, Int
from cas.exceptions import ParserException

"""
stmt    :=  decl | expr
decl    :=  "let" ID ":=" expr
expr    :=  add
add     :=  mult { ( "+" | "-" ) mult }
mult    :=  pow { ( "*" | "/" ) pow }
pow     :=  unary [ "^" pow ]
unary   :=  [ "-" ] atom
atom    :=  call | NUMBER | var | "(" expr ")"
var     :=  CHAR
call    :=  ID "(" [ expr  { "," expr } ] ")"
"""


class Parser:

    _FUNCTIONS = ["sin", "cos", "tan", "sqrt"]
    _SAVED_EXPR = ["malaise"]

    def __init__(self) -> None:
        self._current = 0

    def parse(self, tokens) -> Stmt:
        """Parse tokens into meaningful syntax trees."""
        self._tokens = tokens
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
        """Get multiplication expression. Handles implicit multiplication.
        3x^2 + xsin(x) - sqrt(x)x + abc/23x - 9quadratic + 1/9
        """
        expr = self._pow()
        factors = []

        while self._match(TokenType.STAR, TokenType.SLASH):
            if self._previous().type == TokenType.SLASH:
                factors.append(self._pow())  # Gotta figure out how to make this negative
            else:
                factors.append(self._pow())

        if factors:
            return Mult(expr, *factors)
        return expr

    def _expandIdent(self) -> None:
        """Given an identifier, discern between saved expressions, function calls, and variables."""
        pass

    def _pow(self) -> Expr:
        """Get power expression."""
        expr = self._unary()
        if self._match(TokenType.CARAT):
            return Pow(self._pow())
        return expr

    def _unary(self) -> Expr:
        """Get unary expression."""
        if self._match(TokenType.MINUS):
            return Mult(Int("-1"), self._atom())
        return self._atom()

    def _atom(self) -> Expr:
        """Get atom (smallest) expression."""

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


if __name__ == "__main__":
    pass
