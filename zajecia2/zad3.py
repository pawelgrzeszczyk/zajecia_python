#generator ciagu fibo

def generator():
    p = 0
    n = 1
    yield p
    yield n
    while True:
        t= p+n
        p=n
        n=t
        yield n
f = generator()
print f.next()
print f.next()
print f.next()
print f.next()
