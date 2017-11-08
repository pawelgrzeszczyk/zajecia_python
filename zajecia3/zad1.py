#zaimplementuj klase "liczba zespolona". Klasa ma miec moizliwosc dodawania, odejmowania,mnozenia, dzielenia oraz
# przypisywania z wykorzystywaniem standardowych operatorow.
#Dodatkowo ma posiadac funkcje "modul" obliczajac moduly liczby zespolonej oraz mozliwosc porownywania go
#rowniez przy pomocy standardowycho peratorow logicznych.
#Po przekazaniu obiektu do funkcji print na zostac ona wyswietlona na ekranie
import math
class liczbaZespolona(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return liczbaZespolona(self.re + other.re, self.im + other.im )
    def __mul__(self, other):
        #return liczbaZespolona(((self.re * other.re)-(self.re * other.re)),((self.re * other.im)+(self.re *other.im)))
        return liczbaZespolona(self.re * other.re, self.im * other.im)
    def __div__(self, other):
        return liczbaZespolona(self.re / other.re, self.im / other.im)
    def __sub__(self, other):
        return liczbaZespolona(self.re - other.re, self.im - other.im)
    def __mod__(self, other):
        #return liczbaZespolona(math.sqrt(((self.re)**2), (self.im)**2))
        return liczbaZespolona(self.re % other.re, self.im % other.im)


a = liczbaZespolona(2,4) + liczbaZespolona(7,1)
print "dodawanie %d + %di" % (a.re, a.im)
b = liczbaZespolona(2,4) - liczbaZespolona(7,1)
print "odejmowanie %d - %di" % (b.re, b.im)
c  = liczbaZespolona(2,4) * liczbaZespolona(7,1)
print "mnozenie %d * %di" % (c.re, c.im)
d = liczbaZespolona(2,4) / liczbaZespolona(7,1)
print "dzielenie %d / %di" %(d.re, d.im)
e =liczbaZespolona(2,4) % liczbaZespolona(7,1)
print "modul %d %di" %(e.re, e.im)