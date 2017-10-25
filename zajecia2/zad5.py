#zaimplementuj funkcje ktora przyjmuje liste punktow na plaszczyznie w postaci krotek
#oraz punkt kontrolny. Funkcja ma zwrocic liste krotek w postaci (odleglosc, punkt(x,y))
#w kolejnosci od najblizszego do najdalszego pomiedzy elementami z listy a punktem kontrolnym
import math
lista = [(4,2), (6,8), (1,5)]
k = [(1,2)]
def odleglosc(p1x,p1y,p2x,p2y):
    return round(math.sqrt(((p2x-p1x)**2)+((p2y-p1y)**2)),2)
def odleglosc2(p1=(),p2=()):
    return math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
def fun(lista, k):
    return  [(odleglosc2(lista[i],k[i]),k) for i in lista]

print odleglosc(4,2,1,2)
print odleglosc2(lista[1],k[0])
print fun(lista,k)

