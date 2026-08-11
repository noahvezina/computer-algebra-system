import cmd

from cas.interpreter.lexer import Lexer
from cas.interpreter.parser import Parser
from cas.exceptions import LexerException, ParserException


class ComputerAlegbraSystem(cmd.Cmd):

    intro = "Computer Algebra System in Python."
    prompt = ">>> "

    # Static function names (TODO might be imported from a different file later)
    func_names = ["sin", "cos", "tan", "sqrt", "diff"]

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

        # Dictionary to keep track of user-written saved expressions
        self.decls = {}

        # Dictionary to keep track of reserved names by type
        self.names = {
            "decl": list(self.decls.keys()),
            "func": self.func_names,
            "all": list(self.decls.keys()) + self.func_names
        }

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

        print(f"TOKENS: {", ".join(list(map(str, tokens)))}")

        # Try to parse tokens
        parser = Parser()
        try:
            ast = parser.parse(tokens, self.names, self.decls)
        except ParserException as error:
            self.printError(error.message, error.column)
            return None
        
        print(f"AST: {ast}")

    def printError(self, message: str, column: int = -1) -> None:
        if column != -1:
            print(f"Error [col {column}]: {message}")
        else:
            print(f"Error: {message}")


if __name__ == "__main__":
    cas = ComputerAlegbraSystem()
    cas.cmdloop()
