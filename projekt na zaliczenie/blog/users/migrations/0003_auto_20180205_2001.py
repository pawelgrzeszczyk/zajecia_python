# Generated by Django 2.0.1 on 2018-02-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180202_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
    ]
