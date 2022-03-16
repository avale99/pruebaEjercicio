# Generated by Django 2.2.12 on 2022-03-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coche', '0005_auto_20220316_1253'),
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='coches',
        ),
        migrations.AddField(
            model_name='modelo',
            name='coches',
            field=models.ManyToManyField(blank=True, related_name='coche', to='coche.Coche', verbose_name='Coches'),
        ),
    ]