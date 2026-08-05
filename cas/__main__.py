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

    lexer = Lexer(user_input)

    try:
        tokens = lexer.scanTokens()
    except LexerException as error:
        print(f"Error [col {error.column}]: {error.message}")
        return None

    print(tokens)


if __name__ == "__main__":
    ComputerAlegbraSystem().cmdloop()
