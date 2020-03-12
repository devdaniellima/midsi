import os
from wsmlparser.parser import *

reasoner = Reasoner()
reasoner.load('wsmlcodes/ont2-DeviceDiscovery/DeviceDiscoveryInstancesDefault.wsml')
# print(reasoner.getAxioms())
# print(reasoner.getFacts())
# print(reasoner.execute('?disp memberOf Lamp'))
print(reasoner.execute('getServices(79,42,360,?disp,?service,?link,?reqModel)'))
# print(reasoner.execute('devices(?disp)'))
# print(reasoner.execute('proximosDef(?x,?y,?z)'))
# print(reasoner.execute('cityIsOnContinent(?city, ?continent)'))
# print(reasoner.execute('?disp[posx hasValue ?x] memberOf Lamp and (?x*0) =< 1'))
#print(reasoner.executeProlog('sqrt(9)'))

# x - 80
# y - 50

# w
# z

# (w-x)*(w-x)+(z-y)*(z-y) < 20*20