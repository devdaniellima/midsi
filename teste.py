import time
from wsmlparser.parser import *

reasoner = Reasoner()
reasoner.load('wsmlcodes/fatorial.wsml')
#print(reasoner.execute("memberOf(Europe,'Continent')"))
print(reasoner.execute("isLocalDef(X)"))