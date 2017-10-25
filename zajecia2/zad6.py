#napisz generator ktory bedzie zwaracal nazwy kolenych plikow z katalogu o podanum rozszerzeniu
#Rozszerzenie oraz sciezke podaje uzytkownik w konsoli
from os import listdir


def generator(s,r):
    lista = listdir(s)
    for x in range(len(lista)):
        if lista[x].__contains__(r):
            yield lista[x]


f = generator("C:\Users\Pawel\Desktop\Python\zajecia_python\zajecia_python\zajecia2",'.py')
print f.next()
print f.next()
print f.next()