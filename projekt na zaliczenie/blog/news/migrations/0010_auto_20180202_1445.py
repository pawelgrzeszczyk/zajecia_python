# Generated by Django 2.0.1 on 2018-02-02 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_delete_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='autor',
        ),
        migrations.AddField(
            model_name='news',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
