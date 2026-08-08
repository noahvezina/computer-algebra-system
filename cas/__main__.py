import cmd

from cas.interpreter.lexer import Lexer
from cas.interpreter.parser import Parser
from cas.exceptions import LexerException, ParserException


class ComputerAlegbraSystem(cmd.Cmd):

    intro = "Computer Algebra System in Python."
    prompt = ">>> "

    # Static function names --- maybe this should be imported from functions.py when written
    func_names = ["sin", "cos", "tan", "sqrt"]

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

        # Storing session context
        self.context = {
            "func_names": self.func_names,
            "saved_exprs": []
            }

    def default(self, line: str) -> None:
        """Run line."""
        self.run(line)
        return None

    def do_quit(self, line: str) -> None:
        """Exit the REPL."""
        return True

    def run(self, user_input: str) -> None:

        lexer = Lexer()
        try:
            tokens = lexer.tokenize(user_input)
        except LexerException as error:
            self.printError(error.message, error.column)

        parser = Parser()
        try:
            ast = parser.parse(tokens, self.context)
        except ParserException as error:
            self.printError(error.message, error.column)

        print("Tokens")

    def printError(message: str, column: int = -1) -> None:
        if column:
            print(f"Error [col {column}]: {message}")
        else:
            print(f"Error: {message}")


if __name__ == "__main__":
    cas = ComputerAlegbraSystem()
    cas.cmdloop()
