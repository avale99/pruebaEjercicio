from django.contrib import admin
from .models import Marca

class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'fundador',
        'fecha_fundacion',
        'telefono_atencion',
        'get_modelos',
    )

    #
    search_fields = ('nombre',)
    list_filter = ('modelos',)


admin.site.register(Marca, MarcaAdmin)