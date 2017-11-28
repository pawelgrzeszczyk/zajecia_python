#Napisz funkcje ktora pobierze od uzytkownika liczbe i wiswietli jej pierwiastek.
# Obsluz wszystkie wykatki ktore moga wystapic w wyniku dizalania programu

import math




def pierwiastek():
    try:
        liczba = input()
        wynik = math.sqrt(liczba)
    except Exception as ex:
        print ex
    else:
        return wynik




print pierwiastek()



