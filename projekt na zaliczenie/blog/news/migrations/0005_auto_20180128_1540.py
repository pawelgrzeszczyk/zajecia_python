# Generated by Django 2.0.1 on 2018-01-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180128_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='icon',
            new_name='ikona',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='odnosnik',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='posted_date',
            new_name='data_publikacji',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='categories',
            new_name='kategoiria',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='slug',
            new_name='odnosnik',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='tytul',
        ),
        migrations.AlterField(
            model_name='news',
            name='autor',
            field=models.ManyToManyField(to='news.Autor', verbose_name='Autor imie'),
        ),
    ]
