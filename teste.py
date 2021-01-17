from wsmlparser.parser import *

reasoner = Reasoner()

reasoner.load('wsmlcodes/ont1-ShipmentOntology/ShipmentOntology.wsml')

#print(reasoner.executeProlog('relationType(X,Y)'))