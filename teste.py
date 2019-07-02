from wsmlparser.parser import *
from pydatalog.pyDatalog.pyDatalog import assert_fact, load, ask

lexer = Lexer('wsmlcodes/OntologiaMundo.wsml')
knowledge = Knowledge()
container = PyDatalogAnalysis(knowledge)

parser = Parser(lexer)
head = parser.parse()
head.apply(container)

for fact in container.knowledge.facts:
    for asserts in container.knowledge.facts[fact]:
        assert_fact(fact,*asserts)
    
for fact in container.knowledge.facts:
    print(fact)
    print(container.knowledge.facts[fact])
    print()

# print(ask("memberOf(X,Y)"))
