# Generated by Django 2.2.12 on 2022-03-16 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_auto_20220316_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marca.Marca', verbose_name='Marca'),
        ),
    ]
