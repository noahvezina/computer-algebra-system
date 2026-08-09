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
    """A parser that transforms tokens into a meaningful AST."""

    def __init__(self) -> None:
        self._current = 0

    def parse(self, tokens: list[Token], context: dict[list]) -> Stmt:
        """Parse tokens into meaningful syntax trees using recursive descent."""
        self._tokens = tokens
        self._context = context

        self._rewrite()

        # if self._match(TokenType.LET):
        #     return self._decl()
        # return self._expr()

    def _rewrite(self) -> None:
        """A two-pass rewrite. Chop up identifiers (variables, function calls, and saved expressions) then add implicit multiplication tokens where suitable."""

        # We iterate in reverse so that the index stays accurate when adding elements to the list
        for i in reversed(range(len(self._tokens))):
            if self._tokens[i].type == TokenType.IDENTIFIER:
                text = self._tokens[i].text
                new_identifiers = self._chopIdentifiers(text)
                self._tokens[i:i + 1] = new_identifiers
            # We do not want to break up declaraction names
            if self._tokens[i].type == TokenType.COLON_EQUALS:
                break

        # Accepted implicit multiplication token pairs (i.e. if a NUMBER token is followed by an IDENTIFIER token, it implies multiplication)
        implicits = {
            TokenType.NUMBER: [TokenType.IDENTIFIER, TokenType.L_PAREN],
            TokenType.IDENTIFIER: [TokenType.IDENTIFIER, TokenType.NUMBER, TokenType.L_PAREN],
            TokenType.R_PAREN: [TokenType.IDENTIFIER, TokenType.NUMBER, TokenType.L_PAREN]
            }

        # Same reverse idea here, but note that the implicits dictionary is relative to the forward direction
        for i in reversed(range(1, len(self._tokens))):
            left = self._tokens[i - 1]
            right = self._tokens[i]
            if left.text in self._context["func_names"]:
                continue
            elif left.type in implicits and right.type in implicits[left.type]:
                implicit_token = Token(TokenType.IMPLICIT, "")
                self._tokens.insert(i, implicit_token)

    def _chopIdentifiers(self, text: str) -> list[Token]:
        """Take apart an indentifier into variables, function calls, and saved expressions."""
        substring_start = 0
        new_identifiers = []

        while substring_start < len(text):
            substring_end = substring_start + 1
            substring_found = False
            # Looking for multi-character substrings
            while substring_end <= len(text):
                if text[substring_start:substring_end] in self._context["all_reserved"]:
                    new_token = Token(TokenType.IDENTIFIER, text[substring_start:substring_end])
                    new_identifiers.append(new_token)
                    substring_start = substring_end
                    substring_found = True
                else:
                    substring_end += 1
            # None found, so we'll add a single-char substring
            if not substring_found:
                substring_end = substring_start + 1
                new_token = Token(TokenType.IDENTIFIER, text[substring_start:substring_end])
                new_identifiers.append(new_token)
                substring_start = substring_end

        return new_identifiers

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
                terms.append(self._mult())  # TODO Gotta figure out how to make this negative
            else:
                terms.append(self._mult())

        if terms:
            return Add(expr, *terms)
        return expr

    def _mult(self) -> Expr:
        """Get multiplication expression. Handles implicit multiplication."""
        expr = self._pow()
        factors = []

        while self._match(TokenType.STAR, TokenType.SLASH, TokenType.IMPLICIT):
            if self._previous().type == TokenType.SLASH:
                factors.append(self._pow())  # TODO Gotta figure out how to make this negative
            else:
                factors.append(self._pow())

        if factors:
            return Mult(expr, *factors)
        return expr

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
        # TODO implement atom

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
        """Check if the next token is of any of the given types, if so it advances to the next token."""
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
        raise ParserException(message)

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
    parser = Parser()
