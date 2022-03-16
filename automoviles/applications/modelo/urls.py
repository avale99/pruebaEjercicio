from django.contrib import admin
from django.urls import path
from . import views

app_name = "modelo_app"

urlpatterns = [
    path('lista-modelos/', views.ListModelosListView.as_view(), name="list_modelos"),
    path('registrar-modelo/', views.ModeloCreateView.as_view(), name="regist_modelos"),
    path('editar-modelo/<pk>/', views.ModeloUpdateView.as_view(), name="edit_modelos"),
    path('eliminar-modelo/<pk>/', views.ModeloDeleteView.as_view(), name="delete_modelos"),
]