# External imports
import cmd

# Interpreter imports
from cas.interpreter.lexer import Lexer
from cas.interpreter.parser import Parser
from cas.interpreter.print import prettyPrint

# Math imports
from cas.math.evaluate import evaluate, funcs

# Exceptions
from cas.exceptions import LexerException, ParserException


class ComputerAlegbraSystem(cmd.Cmd):

    intro = "Computer Algebra System in Python."
    prompt = ">>> "

    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)

        # Dictionary to keep track of user-written saved expressions
        self.decls = {}

        # Setup dictionary to keep track of used names
        self.updateNames()

    def default(self, line: str) -> None:
        """Run line."""
        self.run(line)
        return None

    def do_quit(self, line: str) -> bool:
        """Exit the REPL."""
        return True

    def do_EOF(self, line: str) -> bool:
        """Exit the REPL."""
        return True

    def run(self, user_input: str) -> None:

        # Try to tokenize user input
        lexer = Lexer()
        try:
            tokens = lexer.tokenize(user_input)
        except LexerException as error:
            self.printError(error.message, error.column)
            return None

        # Try to parse tokens
        parser = Parser()
        try:
            ast = parser.parse(tokens, self.names, self.decls)
        except ParserException as error:
            self.printError(error.message, error.column)
            return None

        # Evaluate
        evaluated_expr = evaluate(ast, self.decls)

        # Pretty print
        print(f"{prettyPrint(evaluated_expr)}")

        # Update names
        self.updateNames()

    def updateNames(self) -> None:
        """Set or update the names dictionary."""
        self.names = {"decl": list(self.decls.keys()), "func": list(funcs.keys()), "all": list(self.decls.keys()) + list(funcs.keys())}

    def printError(self, message: str, column: int = -1) -> None:
        if column != -1:
            print(f"Error [col {column}]: {message}")
        else:
            print(f"Error: {message}")


if __name__ == "__main__":
    cas = ComputerAlegbraSystem()
    cas.cmdloop()
