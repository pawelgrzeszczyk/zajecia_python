#Zmodyfikuj powyzsze zadanie tak, by wypisywany tekst byl wysrodkowany (w obrebie zadanych width miejsc na ekranie).

def fun(parametr):
    f  = open(parametr)
    width = input()
    n = f.read()
    n = n.replace('\n',' ')
    print n
    while n:
        print n[:width].center(4)
        n = n[width:]


fun("plik.txt")