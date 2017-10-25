
#listy skladane
liczby = range(0,20)
print liczby
kwadraty = [x**2 for x in liczby]
print kwadraty

#funkcje wyzszego rzedu

def f1(a):
    def f2(b):
        return a - b
    return f2

def f3(c):
    print c(11)
res = f1(5)
print res(10)
f3(res)

#wyrazenia lambda

kwadrat = lambda x: x*x
print kwadrat(2)

#generatory

def generator(n):
    while n:
        print 'Generator start %d'%n
        yield n
        print 'Generator stop %d'%n
        n-=1

#    for x in generator(5):
#        print 'wywolanie %d' %x

gen = generator(5)
print gen.next()
print gen.next()