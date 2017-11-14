# napisz program ktory w parametrze przyjmuje nazwe pliku. Program ma stworzyc slownik w ktorym
# zostanie zliczona ilosc wystapien danego slowa we wczytanym tekscie np
# ala ma
# kota ala
# ala: 2, ma:1 , kota:1


f = open("plik.txt")
plik = f.read()
lista = plik.split()
filtr = [ x for x in lista]
slownik = {}

for x in set(filtr):
    slownik[x] = 0

for k,v in slownik.items():
    for item in lista:
        if item == k:
           slownik[k]+=1


print slownik
f.close()




