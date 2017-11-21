# Napisz program, ktory z zadanego parametrem pliku tekstowego wypisze na
# standardowe wyjscie wszystkie
# poprawne adresy IP (ver4) kazdy w osobnej linii.

import re

wzorzec = re.compile(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$')

f = open("plik.txt")
plik = f.read()
lista = plik.split()

# def sprawdzaj(lista):
#     nowa = []
#     for line in lista:
#         elementy = line.split('.')
#         if len(elementy) != 4:
#            return False
#         for item in elementy:
#             if not 0 <= int(item) <=255:
#                 return False
#         nowa.append(elementy)
#     print nowa

for x in lista :
    ip = re.match(wzorzec,x)
    if ip:
        napis = ip.group()
        print napis

