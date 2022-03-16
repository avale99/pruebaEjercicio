from django.contrib import admin
from .models import Modelo

class ModeloAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'carroceria',
        'marca',
        'get_coches',
    )

    #
    search_fields = ('nombre', 'marca',)
    list_filter = ('marca', 'coches', 'carroceria',)


admin.site.register(Modelo, ModeloAdmin)
