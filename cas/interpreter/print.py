from cas.interpreter.nodes import Expr, Add, Mult, Pow, Num, Var


def prettyPrint(expr: Expr, implicit=True) -> str:
    string = ""
    match expr:
        case Add(terms):
            for i in range(len(terms)):
                string += prettyPrint(terms[i])
                if i != len(terms) - 1:
                    string += " + "
        case Mult(factors):
            for i in range(len(factors)):
                string += prettyPrint(factors[i])
                if not implicit and i != len(factors) - 1:
                    string += "*"
        case Pow(base, exponent):
            string += str(base) + "^" + str(exponent)
        case Num() as num:
            string += str(num)
        case Var() as var:
            string += str(var.symbol)
        case _:
            return "Not implemented yet!"
    return string
