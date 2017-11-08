# #KLASY
# class klasa:
#     zmienna = 5
#     def funkcja(self):
#         print "metoda"
#         print self.zmienna
# obiekt = klasa()
# obiekt.funkcja()
#
# class klasa1:
#     def funkcja1(self, zmienna):
#         print "wywolanie metody %s" %zmienna
#         self.funkcja2()
#     def funkcja2(self):
#         print "funkcja2"
#
#
# obiekt1 = klasa1()
# obiekt1.funkcja1("funkcja")
# #ZMIENNE
# class klasa3:
#     atr1 = None
#     _atr2 = None #prywatna
#     def setAtr2(self, zmienna):
#         self._atr2=zmienna
#     def setAtr3(self, zmienna):
#         self.atr3 = zmienna
#     def add(self):
#         return self.atr1+self._atr2+self.atr3
# obekt3 = klasa3()
# obekt3.atr1 = 4
# obekt3.setAtr2(5)
# obekt3.setAtr3(10)
# obekt3._klasa_atr2 = 8
# print obekt3.add()
# #DZIEDZICZENIE
#
# class samochod:
#     kolor = None
#     def setKolor(self, kolor):
#         self.kolor = kolor
# class osobowy(samochod):
#     marka = "mercedes"
#
# sam = osobowy()
# sam.setKolor("czerwony")
# print ("to jest %s %s") % (sam.kolor, sam.marka)
#
# #FUNKCJE SUPER
#
# class A:
#     def funkcjaA(self):
#         print "wywolanie A"
# class B:
#     def funkcjaA(self):
#         print "wywolanie B"
#         super(B, self).funkcjaA()
# B().funkcjaA()

#metody specjalne

class A:
    def __init__(self, zmienna):
        self.zmienna = zmienna
    def __add__(self, other):
        return self.zmienna + other.zmienna

a = A(5)
b = A(8)
print a+b