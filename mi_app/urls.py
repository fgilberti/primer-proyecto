from django.contrib import admin
from django.urls import path
from mi_app.views import (saludo, saludar_a, mostrar_index)

urlpatterns = [
    path('hola/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('mi-pagina/', mostrar_index)
]
