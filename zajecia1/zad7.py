ciag = raw_input('podaj ciag znakow do szyfrowania: ')


def szyfruj(tekst):
    klucz = 3
    zaszyfrowny = ""
    for i in range(len(tekst)):
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowny += chr(ord(tekst[i]) + klucz - 26)
        else:
            zaszyfrowny += chr(ord(tekst[i]) + klucz)
    return zaszyfrowny

print szyfruj(ciag)