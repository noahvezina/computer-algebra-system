from cas.interpreter.nodes import Stmt, Decl, Expr, Call
from cas.math.diff import diff

funcs = {"diff": diff}


def evaluate(ast: Stmt, decls: dict) -> Expr:
    """Evaluate an abstract syntax tree."""
    match ast:
        case Decl(name, expr):  
            result = evaluate(expr, decls)
            decls[name] = result
            return result
        case Call(name, args):
          return funcs[name](*args)    
        case Call(name, []):
            return funcs[name]()
        case _:
            return ast
