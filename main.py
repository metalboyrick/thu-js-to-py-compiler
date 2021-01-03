import sys
from antlr4 import *
from Js2PyLexer import Js2PyLexer
from Js2PyParser import Js2PyParser
from Js2PyListener import Js2PyListener

"""
add the following in Js2PyListener class
def __init__(self,output):
    self.output = output
    super()
"""

def main(argv):
    input = FileStream(argv[1])
    lexer = Js2PyLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Js2PyParser(stream)
    tree = parser.program()

    with open("output.py","w") as output:
        js2pyListen = Js2PyListener(output)
        walker = ParseTreeWalker()
        walker.walk(js2pyListen, tree)
        
    output.close()      

if __name__ == '__main__':
    main(sys.argv)