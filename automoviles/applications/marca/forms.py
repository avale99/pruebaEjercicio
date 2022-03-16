from django import forms

from .models import Marca

class MarcaForm(forms.ModelForm):
    
    class Meta:
        model = Marca
        fields = (
            'nombre',
            'fundador',
            'fecha_fundacion',
            'telefono_atencion',
            'modelos'
        )
        widgets = {
            'modelos': forms.SelectMultiple(),
            'fecha_fundacion': forms.DateInput(
                attrs= {
                    'placeholder': 'Dia/Mes/Año',
                }
            )
        }