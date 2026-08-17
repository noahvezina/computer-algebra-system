from abc import ABC


class Stmt(ABC):
    """The parent class for declarations and expressions."""


class Decl(Stmt):
    """A reusable call-by-name expression."""

    __match_args__ = ("name", "expr")

    def __init__(self, name: str, expr: Expr) -> None:
        self.name = name
        self.expr = expr

    def __repr__(self) -> str:
        return f"Decl({self.name} => {self.expr})"

class Expr(Stmt, ABC):
    """A base class for all things that can be in an expression."""

    def __init__(self) -> None:
        self.has_parentheses = False


class Add(Expr):
    """An n-ary addition operator."""

    __match_args__ = ("terms",)

    def __init__(self, *terms: Expr) -> None:
        super().__init__()
        self.terms = list(terms)

    def __repr__(self) -> str:
        return f"Add({", ".join(list(map(str, self.terms)))})"


class Mult(Expr):
    """An n-ary multiplication operator."""

    __match_args__ = ("factors",)

    def __init__(self, *factors: Expr) -> None:
        super().__init__()
        self.factors = list(factors)

    def __repr__(self) -> str:
        return f"Mult({", ".join(list(map(str, self.factors)))})"


class Pow(Expr):
    """A binary power operator."""

    __match_args__ = ("base", "exponent")

    def __init__(self, base: Expr, exponent: Expr) -> None:
        super().__init__()
        self.base = base
        self.exponent = exponent

    def __repr__(self) -> str:
        return f"Pow({self.base}, {self.exponent})"


class Call(Expr):
    """A function call."""

    __match_args__ = ("name", "args")

    def __init__(self, name: str, args: list[Expr]) -> None:
        super().__init__()
        self.name = name
        self.args = args

    def __repr__(self) -> str:
        return f"{self.name.title()}({", ".join(list(map(str, self.args)))})"


class Var(Expr):
    """A single-letter variable."""

    __match_args__ = ("symbol",)

    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.symbol = symbol

    def __repr__(self) -> str:
        return f"Var({self.symbol})"


class Num(Expr):
    """A number base-class for rationals and floats."""

    def __init__(self) -> None:
        super().__init__()


class Float(Num):
    """A floating point number."""

    __match_args__ = ("value",)

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = float(value)

    def __repr__(self) -> str:
        return f"Float({self.value})"

class Rational(Num):
    """A rational number."""

    __match_args__ = ("numerator", "denominator")

    def __init__(self, numerator: str, denominator: str) -> None:
        super().__init__()
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __repr__(self) -> str:
        return f"Rational({self.numerator}/{self.denominator})"


class Int(Rational):
    """An integer number."""

    __match_args__ = ("value",)

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Int({self.value})"


class Const(Expr):
    """A constant expression."""

    __match_args__ = ("name",)

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Const({self.name})"


if __name__ == "__main__":
    pass
