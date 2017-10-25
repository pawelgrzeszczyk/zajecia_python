#korzystajac z listy skladnych napisz funkcje ktora stworzy liste n elementow ciagu fibonnacciego. Liczba n podawana jest w konsoli




def fibo(n):
    pierwsze = [0,1]
    nowa = [pierwsze[-1]+pierwsze[-2] for x in range(n)]
    print nowa

fibo(10)