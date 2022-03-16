from django.contrib import admin
from django.urls import path
from . import views

app_name = "marca_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),
    path('lista-marcas/', views.ListMarcasListView.as_view(), name="list_marcas"),
    path('registrar-marca/', views.MarcaCreateView.as_view(), name="regist_marcas"),
    path('editar-marca/<pk>/', views.MarcaUpdateView.as_view(), name="edit_marcas"),
    path('eliminar-marca/<pk>/', views.MarcaDeleteView.as_view(), name="delete_marcas"),
]