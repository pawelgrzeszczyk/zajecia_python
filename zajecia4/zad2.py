# zmodyfikuj pooprzedni program tak aby identycznie zdefiniowany napis byl wczytywany z pliku:
# nazwa pliku podawana jest w parametrze
# k1: w1
# k2: w2
# k3: w3

slownik = {}
f = open("plik.txt")
plik = f.read()
lista = plik.split('\n')

for x in lista:
    elementy = x.split(':')
    slownik[elementy[0]] = elementy[1]
    print slownik


f.close()