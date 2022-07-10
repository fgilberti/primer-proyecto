from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola Mundo {fecha_hora_ahora}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")


def mostrar_index(Request):
    return render(Request, "mi_app/index.html", {"titulo": "Esta es la Primer Website de Fran"})
