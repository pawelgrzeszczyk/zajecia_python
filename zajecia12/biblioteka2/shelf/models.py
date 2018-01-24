from django.db import models

# Create your models here.
class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return "{imie} {nazwisko}".format(imie=self.imie, nazwisko=self.nazwisko)

class Wydawnictwo(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

class Book(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor,
    on_delete=models.CASCADE,)
    wydawnictwo = models.ForeignKey(Wydawnictwo,
    on_delete=models.CASCADE,)

    def __str__(self):
        return self.tytul