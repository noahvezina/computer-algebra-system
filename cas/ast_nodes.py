from abc import ABC


class Stmt(ABC):
    """The parent class for declarations and expressions."""


class Decl(Stmt):
    """A reusable call-by-name expression."""

    def __init__(self, name: str, expr: Expr) -> None:
        self.name = name
        self.expr = expr


class Expr(Stmt, ABC):
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
  


class Var(Expr):
    """A named variable that stores an expression."""  

    def __init__(self, name: str, expr: Expr) -> None:
        self.name = name
        self.expr = expr

if __name__ == "__main__":
    pass
