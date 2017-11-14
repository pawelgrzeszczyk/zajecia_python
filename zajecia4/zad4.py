# napisz program ktory w parametrze otrzymuje nazwe pliku lub znak '-' oraz ciag znakow.
# Program ma wczytac plik i wyswietlic te linie w ktorych znajduje sie podany ciag znakow.
# Jezeli zamiast nazwy pliku jest znak - to linie sa wczytane ze standardowego wejscia.
# Pusta linia konczy wczytywanie

parametr = "-"
ciag = "ala"

if parametr == "-":
    lista = []

    while True:
        napis = raw_input()
        lista.append(napis)
        if napis == "  ":
            break

    for line in lista:
        if line.__contains__(ciag):
            print line



else:
    f = open(parametr)
    plik = f.read()
    lista = plik.split('\n')

    for line in lista:
        elementy = line.split()
        if line.__contains__(ciag):
            print elementy

    f.close()