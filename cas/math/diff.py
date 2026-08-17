from cas.interpreter.nodes import Expr, Add, Mult, Pow, Var, Num, Int


def diff(expr: Expr, var: Var):
    """Differentiate an expression with respect to var."""
    match expr:
        case Add(terms):
            # Sum rule
            result = []
            for term in terms:
                result.append(diff(term, var))
            return Add(*result)
        case Mult(factors):
            # Product rule
            result_terms = []
            for i in range(len(factors)):
                result_factors = []
                for j in range(len(factors)):
                    if i == j:
                        result_factors.append(diff(factors[j], var))
                    else:
                        result_factors.append(factors[j])
                result_terms.append(Mult(*result_factors))
            return Add(*result_terms)
        case Pow(base, exponent):
            # Power rule
            if isinstance(exponent, Num):
                return Mult(diff(base, var), Pow(base, exponent - Int(1)))
        case Num():
            # Number
            return Int("0")
        case Var() as var:
            # Variable
            return Int("1")
        case _:
            return "Not implemented yet"