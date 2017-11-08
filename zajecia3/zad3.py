#zaimplementuj klase samochod posiadajaca prywatne pola maraka,
#pojemnoscBaku, predkoscMaksymalna, zuzyciePaliwa oraz funkcje publiczne konstruyktor
#jedz(predkosc, odleglosc) wyswietlajaca informacje o predkosci ( nie wieksza niz maksymalna)
#czasie podrozy, zuzyciu paliwa oraz ile razy trzeba bedzie tankowac. Jezeli samochod jedzie poniezej
# 30% lub powyzej 80% predkosci maksymalnej to zuzycie paliwa wzrasta o 20%
#nastepnie zdefiniuj klase kabriolet dziedziczaca po samochdzie posiadajaca dodatkowe pole
# otwartDach oraz dwie dodatkowe metody zamknijDach oraz otwotzDach. Jezeli dach jest otwart to zuzycie paliwa
# podczas obliczen w funkcji jedz powinno wzrosnac o 15 %
from __future__ import division
class samochod(object):
    __marka = None
    __pojemnoscBaku = None
    __predkoscMaksymalna = None
    __zuzyciePaliwa = None

    def __init__(self, marka, pojemnoscBaku, predkoscMaksymalna, zuzyciePaliwa):
        self.__marka = marka
        self.__pojemnoscBaku = pojemnoscBaku
        self.__predkoscMaksymalna = predkoscMaksymalna
        self.__zuzyciePaliwa = zuzyciePaliwa

    def jedz(self, predkosc, odleglosc):
        print ("marka pojazdu: %s" %self.__marka)
        if predkosc < self.__predkoscMaksymalna:
            print ("predkosc wynosi: %d" % predkosc)
        else:
            predkosc = self.__predkoscMaksymalna - predkosc
            print  ("predkosc wynosi: %d" % predkosc)

        czas = odleglosc / predkosc
        print ("czas podrozy wynosi: %.2f " % czas)

        #self.__zuzyciePaliwa = (self.__pojemnoscBaku / odleglosc)*100
        if (self.__predkoscMaksymalna*0.3) > predkosc  or predkosc > (self.__predkoscMaksymalna*0.8):
            self.__zuzyciePaliwa += self.__zuzyciePaliwa * 0.2
            print ("zuzycie paliwa wynosi: %.2f" % self.__zuzyciePaliwa)
        else:
            print ("zuzycie paliwa wynosi: %.2f" % self.__zuzyciePaliwa)
        tankuj = self.__zuzyciePaliwa * (round(odleglosc/100))
        tankowania = 1
        if tankuj > self.__pojemnoscBaku:
            tankowania +=1
        print ("ilosc tankowan wynosi: %d" %tankowania)



class kabriolet(samochod):
    __otwartyDach = None
    def __init__(self, otwartyDach):
        self.__otwartyDach = otwartyDach
        super(kabriolet, self).jedz()
    def zamknijDach(self):
        self.__otwartyDach = False
        return self.__otwartyDach
    def otworzDach(self):
        self.__otwartyDach = True
        return self.__otwartyDach

sam = samochod("BMW",60,220,10)
sam.jedz(200,500)

sam2 = samochod("Ford",100,300,15)
sam2.jedz(150,50)