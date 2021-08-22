from wsmlparser.parser import *

reasoner = Reasoner()
reasoner.load('wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml')

print(reasoner.execute('cityIsOnContinent(?city,?continent)'))