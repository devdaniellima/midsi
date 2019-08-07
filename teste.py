import time
from wsmlparser.parser import *

reasoner = Reasoner()
reasoner.load('wsmlcodes/fatorial.wsml')
#reasoner.load('wsmlcodes/OntologiaMundo.wsml')
#print(reasoner.execute("memberOf(Europe,'Continent')"))
print(reasoner.execute("fatorial(20,X)"))