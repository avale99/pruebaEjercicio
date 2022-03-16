from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Marca
from .forms import MarcaForm

class InicioView(TemplateView):
    template_name = 'inicio.html'

# Create your views here.
class ListMarcasListView(ListView):
    context_object_name = 'lista_marcas'
    template_name = 'marca/lista.html'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        return Marca.objects.listar_marcas(palabra_clave)

class MarcaCreateView(CreateView):
    model = Marca
    template_name = "marca/register.html"
    form_class = MarcaForm
    success_url = reverse_lazy('marca_app:list_marcas')

    def form_valid(self, form):
        marca = form.save()
        marca.save()
        return super(MarcaCreateView, self).form_valid(form)

#UPDATE
class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = "marca/editar.html"
    fields = [
        'nombre',
        'fundador',
        'fecha_fundacion',
        'telefono_atencion',
        'modelos'
    ]
    success_url = reverse_lazy('marca_app:list_marcas')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = "marca/delete.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('marca_app:list_marcas')
        self.object.delete()
        return HttpResponseRedirect(success_url)
