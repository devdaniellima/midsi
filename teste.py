from wsmlparser.parser import *
from types import *

lexer = Lexer('wsmlcodes/OntologiaMundo.wsml')

# container = Analysis()

parser = Parser(lexer)
head = parser.parse()
print(head)