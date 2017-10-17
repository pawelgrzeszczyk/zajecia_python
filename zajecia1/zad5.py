n = input('podaj ilosc ')
tab = []
for x in range(0,n):
    liczba = input()
    tab.append(liczba)

kierunek = input('podaj kierunek sortowania 1 malejaco 2 rosnaco')
zakres1 = input('podaj zakres od kiedy wyswietlac ')
zakres2 = input('podaj zakres do kiedy wyswietlac ')




for x in range(zakres1,zakres2):
   if kierunek == 1:
       tab.sort(reverse=True)
       print tab[x]
   else:
       tab.sort()
       print tab[x]


