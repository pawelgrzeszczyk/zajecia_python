#SKRYPTY
#chmod -x test.py


# import sys
# print  sys.argv

#SLOWNIKI

slownik = {
     'kl' : 'w1',
     2: [1,2,3],
     (3,2,1) : 'X',
 }

slownik ['self'] = slownik
slownik ['nowy'] = slownik

#print slownik.get['xyz']
#print slownik.get['xyz','BD']

for x in slownik.items():
    print x
    print slownik.keys()
    print slownik.values()
    print slownik.items()

#NAPISY
napis1 = "abc"
napis = '''a
b
c
asd'''
print napis

znaki = ['a','b','c']
napiss = ''
for x in znaki:
    napiss += x

print napiss #nieoptymalne

znak = 'X'
print ''.join(znaki)
print ''.join(znaki)
print  znak.join(znaki)

nap = 'ala ma kota'
nap2 = 'ala.ma.kota'
print nap.split()
print nap2.split('.')

#PLIKI
f= open("plik.txt")
for line in f:
    print line
print f.read()
f.close()

ff = open("plik.txt","w")
ff.write("test")
ff.close()

