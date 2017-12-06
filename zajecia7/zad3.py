# napisz program posiadajacy funkcje ktora oblicza rozklad liczby podanej w argumencie na czynniki pierwsze
# i zwraca wynikw postaci par krotek [(p1,w1), (p2,w2)..] takich ze n= p1^w1 * p2^w2
# przyklad
# rozklad (756)
# [(2,2),(3,3),(7,1)]

from math import *


def rozklad(x):
    if x <= 0:
        return 0
    i = 2
    e = floor(sqrt(x))
    r = []

    while i <= e:
        if x % i == 0:
            r.append(i)
            x /= i
        else:
            i += 1
    if x > 1: r.append(x)

    licznik = 1
    krotki = []

    for x in range(1,len(r)):
        if r[x] == r[x-1]:
            licznik +=1
        else:
            krotki.append((r[x-1],licznik))
            licznik = 1
    krotki.append((r[len(r)-1], licznik))
    return krotki

print rozklad(756)


