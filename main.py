import sys
from antlr4 import *
from Js2PyLexer import Js2PyLexer
from Js2PyParser import Js2PyParser
from Js2PyChatListener import Js2PyChatListener

def main(argv):
    input = FileStream(argv[1])
    lexer = ChatLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ChatParser(stream)
    tree = parser.chat()

    output = open("output.py","w")
    
    htmlChat = HtmlChatListener(output)
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)
        
    output.close()      

if __name__ == '__main__':
    main(sys.argv)