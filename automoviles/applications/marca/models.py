from django.db import models
from .managers import MarcaManager

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField('Marca', max_length=50, unique=True)
    fundador = models.CharField('Fundador', max_length=50)
    fecha_fundacion = models.DateField('Fundacion')
    telefono_atencion = models.IntegerField('Telefono', unique=True)
    modelos = models.ManyToManyField('modelo.Modelo', related_name='modelo',verbose_name='Modelos' , blank=True)

    objects = MarcaManager()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']

    def __str__(self):
        return self.nombre

    def get_modelos(self):
        return " - ".join([str(p) for p in self.modelos.all()])
