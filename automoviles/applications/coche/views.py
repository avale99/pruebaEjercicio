from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Coche
from .forms import CocheForm

# Create your views here.
class ListCochesListView(ListView):
    context_object_name = 'lista_coches'
    template_name = 'coche/lista.html'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        if palabra_clave == '':
            return Coche.objects.listar_coches()
        else:
            return Coche.objects.listar_coches_kword(palabra_clave)

class CocheCreateView(CreateView):
    model = Coche
    template_name = "coche/register.html"
    form_class = CocheForm
    success_url = reverse_lazy('coche_app:list_coches')

    def form_valid(self, form):
        modelo = form.save()
        modelo.save()
        return super(CocheCreateView, self).form_valid(form)

#UPDATE
class CocheUpdateView(UpdateView):
    model = Coche
    template_name = "coche/editar.html"
    fields = [
        'matricula',
        'fecha_creacion',
        'marca',
        'modelo',
    ]
    success_url = reverse_lazy('coche_app:list_coches')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['name']
        return super().post(request, *args, **kwargs)

#DELETE
class CocheDeleteView(DeleteView):
    model = Coche
    template_name = "coche/delete.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('coche_app:list_coches')
        self.object.delete()
        return HttpResponseRedirect(success_url)
