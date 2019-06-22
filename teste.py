from wsmlparser.parser import *

lexer = Lexer('wsmlcodes/OntologiaMundo.wsml')

parser = Parser(lexer)
head = parser.parse()
