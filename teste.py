import time
from wsmlparser.parser import *

reasoner = Reasoner()
#reasoner.printLogLoading = True
reasoner.load('wsmlcodes/CasaAutomatizada.wsml')
reasoner.load('wsmlcodes/OntologiaMundo.wsml')
reasoner.load('wsmlcodes/fatorial.wsml')

print(reasoner.execute("memberOf(X,'Comodos')"))
#print()
#print(reasoner.execute("cityIsInCountry(X,Y)"))
print()
print(reasoner.execute("fatorial(10,X)"))