# # napisz funkcje ktora wczytuje plik oraz wczytuje zmienna width w kosnoli,
# nastepnie wyswietla tekst tak ze w jednej linii bedzie nie wiecej niz width znakow

def fun(parametr):
    f  = open(parametr)
    width = input()
    n = f.read()
    n = n.replace('\n',' ')
    print n
    while n:
        print n[:width]
        n = n[width:]


fun("plik.txt")

# napis = '''aa
# bb
# bb
# cc'''
#
# napis = napis.replace('\n',' ')
# print napis
# while napis:
#     print napis[:2].center(4) #zad2
#     napis = napis[2:]