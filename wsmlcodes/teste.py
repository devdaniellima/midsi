import time
from pyswip import Prolog
prolog = Prolog()

prolog.assertz('fun(X) :- red(X),car(X)')
prolog.assertz('happy(X) :- red(X);car(X)')

prolog.assertz('car(vw_beatle)')
prolog.assertz('car(ferrari)')
#prolog.assertz('car(hyundai)')
prolog.assertz('bike(harley_davidson)')
prolog.assertz('red(ferrari)')
prolog.assertz('red(vw_beatle)')
prolog.assertz('blue(hyundai)')

#print(list(prolog.query('car(Which)')))
#print(list(prolog.query('fun(Which)')))
print(list(prolog.query('car(ferrari)')))
inicio = time.time()
prolog.assertz('fatorial(0,1)')
prolog.assertz('fatorial(N,F) :- N>0,N1 is (N-1),fatorial(N1,F1),F is (N*F1)')
#print(list(prolog.query('fatorial(0,X)')))
print(list(prolog.query('fatorial(20,X)')))
fim = time.time()

print(fim-inicio)
