
from django.db import models

# Create your models here.

from users.models import BlogUser

class Category(models.Model):
    nazwa = models.CharField('Nazwa Kategorii', max_length=100)
    odnosnik = models.SlugField('Odnośnik', unique=True, max_length=100)
    ikona = models.ImageField('Ikonka Kategorii', upload_to='icons',blank=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.nazwa


class News(models.Model):
    tytul = models.CharField('Tytuł', max_length=255)
    odnosnik = models.SlugField('Odnośnik', max_length=255, unique=True)
    text = models.TextField(verbose_name='Treść')
    kategoiria = models.ManyToManyField(Category, verbose_name='Kategorie')
    data_publikacji = models.DateTimeField('Data dodania', auto_now_add=True)
    autor = models.ForeignKey(BlogUser,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"

    def __str__(self):
        return self.tytul

