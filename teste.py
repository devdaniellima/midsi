from wsmlparser.parser import *

reasoner = Reasoner()

#reasoner.load('wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml')
reasoner.load('wsmlcodes/RepositoryOntology/Repository.wsml')

print(reasoner.execute('packageDependences("code",?dependency)'))
print(reasoner.execute('packageUri("code",?repo,?package)'))