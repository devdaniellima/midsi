import time
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

for axiom in container.knowledge.axioms:
        load(axiom)

inicio = time.time()

# print(ask("cityIsOnContinentDef()"))
# print(ask("membroDeDef(X,Y)"))
fim = time.time()

print(inicio)
print(fim)
print(fim-inicio)