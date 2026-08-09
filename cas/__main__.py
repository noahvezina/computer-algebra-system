import cmd

from cas.interpreter.lexer import Lexer
from cas.interpreter.parser import Parser
from cas.exceptions import LexerException, ParserException


class ComputerAlegbraSystem(cmd.Cmd):

    intro = "Computer Algebra System in Python."
    prompt = ">>> "

    # Static function names (might be imported from a different file later)
    func_names = ["sin", "cos", "tan", "sqrt", "diff"]

    def __init__(self, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)

        # Storing session context
        self.decl_names = ["goose"] # Test name
        self.context = {
                "func_names": self.func_names,
                "decl_names": self.decl_names,
                "all_reserved": self.func_names + self.decl_names
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

        # Try to parse tokens
        parser = Parser()
        try:
            ast = parser.parse(tokens, self.context["reserved_ids"])
        except ParserException as error:
            self.printError(error.message, error.column)
            return None
        
        print(ast)

    def printError(self, message: str, column: int = -1) -> None:
        if column != -1:
            print(f"Error [col {column}]: {message}")
        else:
            print(f"Error: {message}")


if __name__ == "__main__":
    cas = ComputerAlegbraSystem()
    cas.cmdloop()
