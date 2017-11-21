#napisz program ktory magazynuje informacje o posiadanych ksiazkach (tytul,numer ISBN, autor)
#Program ma miec mozlowsc dodawania, usuwaniam, wyswietlania pozycji oraz zapisu stanu programu
#do pliku jak i mozlowsc jego wczytania. Sciezke do pliku podajemy w parametrze uruchomieniowym skryptu//serlizacja
import pickle


class Ksiazka(object):
    tytul = None
    autor = None
    numer = None

    def __init__(self, tytul, autor, numer):
        self.tytul = tytul
        self.autor = autor
        self.numer = numer

def dodawaj(ksiazka, lista):
    lista.append(ksiazka)
    return lista

def usun(ksiazka , lista):
    lista.remove(ksiazka)
    return lista

def zapis(lista, plik):
    pickle.dump(lista, plik)

def wczytaj(plik):
    lista = pickle.load(plik)
    return lista

def wyswietlaj(lista):
    for x in lista:
        print x.tytul
        print x.autor
        print x.numer

plikZ = open("plikZ.txt", "w")
plikW = open("plikW.txt", "r")

lista = []


a = Ksiazka('Ala','Mickiewicz', 112)
b = Ksiazka('Ma', 'Sienkiewicz', 1992)
lista = dodawaj(a, lista)
lista = dodawaj(b, lista)
lista = usun(a, lista)
zapis(lista, plikZ)
lista = wczytaj(plikW)
wyswietlaj(lista)




