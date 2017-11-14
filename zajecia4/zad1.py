# napisz funckje ktora przyjmuje napis w formacie:
# "'k1:w1
# k2:w2
# k3:w3"'
# i zwraca slownik w postaci : 'k1':'w1', 'k2':'w2','k3':'w3'

def fun(napis):
    slownik = {}
    for line in napis.split('\n'):
        elementy = line.split(':')
        slownik[elementy[0]] = elementy[1]
        print slownik
        
napis = '''k1:w1
k2:w2
k3:w3'''
fun(napis)
