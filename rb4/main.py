from antlr4 import *

from gen.rbgramLexer import rbgramLexer
from gen.rbgramParser import rbgramParser
from gen.rbgramMyListener import  rbgramListener

if __name__ == '__main__':
    print('AntLR com Python: ')
    exp = "-4 + 1 ^ 5 - 2\n"
    print(exp)
    data = InputStream(exp)

    # Lexer
    lexer = rbgramLexer(data)
    tokens = CommonTokenStream(lexer)

    # Parser
    parser = rbgramParser(tokens)
    tree = parser.line()

    # Listener
    listener = rbgramListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)