#zaimplementuj funkcje ktora w argumencie otrzymuje funkcje logiczna oraz liste i zwraca liste elementow spelniajacych warunek podany w przekazywanbej funkcji

def logiczna(a):
    return a%2

def testowa(f,n):
    return [i for i in range(0,n+1) if f(i)]


print testowa(logiczna,4)
print testowa(logiczna,5)