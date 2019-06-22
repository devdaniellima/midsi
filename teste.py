from wsmlparser.parser import *
from types import *

lexer = Lexer('wsmlcodes/OntologiaMundoTeste.wsml')

container = Analysis()

parser = Parser(lexer)

head = parser.parse()
head.apply(container)
print(head.getEOF())