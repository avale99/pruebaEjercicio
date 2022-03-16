from django.db import models
from django.db.models import Q

class CocheManager(models.Manager):
    """ Managers para modelo coche """

    def listar_coches(self):
        return self.all()
        '''lista = self.filter(
            marca__nombre=kword
        )
        return lista'''

    def listar_coches_kword(self, kword):
        #return self.all()
        lista = self.filter(
            marca__nombre=kword
        )
        return lista