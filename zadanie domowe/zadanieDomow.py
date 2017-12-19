import re
import urllib
from bs4 import BeautifulSoup
import operator

listaUrl = ["https://www.python.org/about/","https://www.python.org","https://www.python.org/community/","https://www.python.org/events/","https://www.python.org/blogs/"]
lis =[]
ls= []
def pobierzDane(listaUrl):
    poprawneSlowa = []
    licz = 0
    for x in listaUrl:
        html = urllib.urlopen((x)).read()
        soup = BeautifulSoup(html, 'html.parser')
        reg = re.compile(r'[A-Za-z]{3,}$')

        listaText = soup.text
        slowa = listaText.split()
        for e in slowa:
            if re.match(reg, e):
                licz +=1
                zmienMale = e.lower()
                poprawneSlowa.append(zmienMale)


        for item in poprawneSlowa:
            if item in poprawneSlowa:
                lis.append([item,ls])
        ls.append(x)

    print "Ilosc slow: %d" %licz
    return poprawneSlowa

poprawneSlowa = []
poprawneSlowa = pobierzDane(listaUrl)


def wypelnijSlownik():
    slownik = {}
    for x in poprawneSlowa:
     slownik[x] = 0

    for k,v  in slownik.items():
        for item in poprawneSlowa:
            if item == k:
                slownik[k]+=1
    return slownik

def dodajListe(slownik):
    l = []
    for k, v in slownik.items():
        l.append([v, listaUrl])
        for x in range(len(l)):
            slownik[k] = l[x]
    return slownik

def sortuj(slownikDoSortowania):
    listaPosortowana = sorted(slownikDoSortowania.items(), key=operator.itemgetter(1), reverse=True)
    return listaPosortowana

slownikNowy = {}
slownik = {}
slownik = wypelnijSlownik()
listaPosortowana = sortuj(slownik)
slownikNowy = dodajListe(slownik)
lista5 = []

print "Najczesciej wystepujace slowa: "
for j in range(5):
    lista5.append(listaPosortowana[j])
print lista5

try:
    out = raw_input("Podaj slowo: ")
    if out in slownik:
        print slownik.get(out)
    else:
        print "Podane slowo nie wystepuje"

except Exception as ex:
    print ex





