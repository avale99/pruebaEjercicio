# Generated by Django 2.2.12 on 2022-03-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=7, unique=True, verbose_name='Matricula')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha Creacion')),
            ],
            options={
                'verbose_name': 'Coche',
                'verbose_name_plural': 'Coches',
                'ordering': ['id'],
            },
        ),
    ]
