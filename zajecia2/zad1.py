# korzystajac z list skladnych napisz funkcje ktora przyjmuje napis i zwraca liste krotek w postaci (slowo, dlugosc slwoa)

napis = "cos tam ala ma kota"
def ilosc(str):
    slowo = str.split()
    dlugosc_slowa = [ (x,len(x))for x in slowo]
    print dlugosc_slowa
ilosc(napis)