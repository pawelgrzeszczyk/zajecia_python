#zaimplemntuj dwie klasy, Punkt2D i rozszerzajaca ja klase Punkt3D. Kazdy z klas ma miec
# mozliwosc obliczania odleglsoci miedzy dwoma punktami
import math



class Punkt2D(object):
    p1 = None
    p2 = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def odleglosc(self, a, b):
        p1 = b.x - a.x
        p2 = b.y - a.y
        return math.sqrt((p1**2) + (p2**2))

class Punkt3D(Punkt2D):
    def __init__(self,x,y,z):
        super(Punkt3D,self).__init__(x,y)
        self.z = z
        super(Punkt3D,self).odleglosc(x,y)

p2d = Punkt2D(4,5)
p2d2 = Punkt2D(2,1)
wynik = p2d.odleglosc(p2d,p2d2)
print (wynik)
p3d = Punkt3D(1,4,5)
print ("%d %d %d") % (p3d.x, p3d.y, p3d.z)


