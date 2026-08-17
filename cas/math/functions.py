from cas.interpreter.nodes import Call


class Sin(Call):
    """A sine function."""

    def __init__(self, name, args):
        super().__init__("sin", args)

class Cos(Call):
    """A cosine function."""

    def __init__(self, name, args):
            super().__init__("cos", args)


class Tan(Call):
    """A tangent function."""

    def __init__(self, name, args):
            super().__init__("tan", args)


class Sqrt(Call):
    """A squareroot function."""

    def __init__(self, name, args):
            super().__init__("sqrt", args)


class Log(Call):
    """A logarithm function."""

    def __init__(self, name, args):
            super().__init__("log", args)


class Ln(Call):
    """A natural logarithm function."""

    def __init__(self, name, args):
            super().__init__("ln", args)
