import sys
sys.path.append('../')
from wsmlparser.parser import *

reasoner = Reasoner()

#reasoner.load('wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml')
reasoner.load('./Packages.wsml')

#print(reasoner.getFacts())

#print(reasoner.execute('packageDependences("code",?dependency)'))
#print(reasoner.execute('packageUri("code",?repo,?package)'))
print(reasoner.execute("?x memberOf ?y and ( depends(?x, ?z) )"))
#print(reasoner.executeProlog('concept(X)'))
#print(reasoner.executeProlog('relationType(X,Y)'))
