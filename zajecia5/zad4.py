# Napisz walidator dla numerow PESEL ktory sprawdza jego poprawnosc oraz wyluskuje z niego date
# urodzenia w postaci dd-'miesiac'-rrr oraz plec

import re


def sprawdz(pesel):
    if (re.match('[0-9]{11}$', pesel)):
        pass
    else:
        return 0

    l = int(pesel[10])
    sumaKontolna = (
        (l * int(pesel[0])) + (3 * int(pesel[l])) + (7 * int(pesel[2])) + (9 * int(pesel[3])) + (
        (l * int(pesel[4]))) + (
            3 * int(pesel[5])) + (7 * int(pesel[6])) + (9 * int(pesel[7])) + (l * int(pesel[8])) + (3 * int(pesel[9])))
    k = 10 - (sumaKontolna % 10)
    if ((k == 10) or (k == 0)):
        return 0
    else:
        return 1


slownikM = {
    '01' : 'Styczen',
    '02' : 'Luty',
    '03' : 'Marzec',
    '04' : 'Kwiecien',
    '05' : 'Maj',
    '06' : 'Czerwiec',
    '07' : 'Lipiec',
    '08' : 'Sierpien',
    '09' : 'Wrzesien',
    '10' : 'Pazdziernik',
    '11' : 'Listopad',
    '12' : 'Grudzien'
}

pesel = "94080208054"
p = int(pesel[9]) % 2
r = int(pesel[0:2])
m = pesel[2:4]
d = pesel[4:6]


if (sprawdz(pesel)):
    if p == 1:
        plec = "Mezczyzna"
    else:
        plec = "Kobieta"

    if (r < 99 and r > 10):
        pr = 19
    else:
        pr = 20

    for item,k in slownikM.items():
        if item == m:
            mies = slownikM[item]
else:
    print "zly PESEL"




print 'Twoja data urodzenia: '+d+'-'+mies+'-'+str(pr)+str(r)
print "Twoja plec to: %s" %plec