import cmd

from cas.interpreter.lexer import Lexer
from cas.interpreter.parser import Parser
from cas.exceptions import LexerException, ParserException


class ComputerAlegbraSystem(cmd.Cmd):

    intro = "Computer Algebra System in Python."
    prompt = ">>> "

    def default(self, line: str) -> None:
        """Run line."""
        return run(line)

    def do_quit(self, line: str) -> None:
        """Exit the REPL."""
        return True


def run(user_input):

    lexer = Lexer()
    try:
        tokens = lexer.tokenize(user_input)
    except LexerException as error:
        printError(error.column, error.message)
        return None

    parser = Parser()
    try:
        ast = parser.parse(tokens)
    except ParserException as error:
        printError(error.column, error.message)
        return None

    print("Tokens")


def printError(column: int, message: str) -> None:
    print(f"Error [col {column}]: {message}")


if __name__ == "__main__":
    ComputerAlegbraSystem().cmdloop()
