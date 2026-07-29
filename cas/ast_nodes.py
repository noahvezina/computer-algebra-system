from abc import ABC


class Decl:
    """A reusable call-by-name expression."""

    def __init__(self, name: str, expr: Expr) -> None:
        self.name = name
        self.expr = expr


class Expr(ABC):
    """A base class for all things that can be in an expression."""


class Add(Expr):
    """An n-ary addition operator."""

    def __init__(self, *terms: Expr) -> None:
        self.terms = list(terms)


class Mult(Expr):
    """An n-ary multiplication operator."""

    def __init__(self, *factors: Expr) -> None:
        self.factors = list(factors)


class Pow(Expr):
    """A binary power operator."""

    def __init__(self, base: Expr, exponent: Expr) -> None:
        self.base = base
        self.exponent = exponent


class Fract(Expr):
    """A binary fraction operator."""

    def __init__(self, numerator: Expr, denominator: Expr) -> None:
        self.numerator = numerator
        self.denominator = denominator


class Fact(Expr):
    """A unary factorial operator."""

    def __init__(self, arg: Expr) -> None:
        self.arg = arg


if __name__ == "__main__":
    pass
