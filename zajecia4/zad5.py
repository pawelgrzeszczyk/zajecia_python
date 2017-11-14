# napisz program ktory w parametrze otrzymuje dwie nazwy plikow.
# Program ma wczytac jeden plik, zaszyfrowac go szyfrem cezara i zapisac pod nowa nazwa z parametru

def szyfruj(tekst):
    klucz = 1
    zaszyfrowny = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowny += chr(ord(tekst[i]) + klucz - 26)
        else:
            zaszyfrowny += chr(ord(tekst[i]) + klucz)
    return zaszyfrowny
paramter1 = "plik.txt"
parametr2 = "plik2.txt"

f = open(paramter1)
n = open(parametr2, "w")
plik = f.read()
lista = plik.split('\n')
print lista
for line in lista :
    print szyfruj(line)
    n.write(szyfruj(line))
    n.write('\n')

f.close()
n.close()