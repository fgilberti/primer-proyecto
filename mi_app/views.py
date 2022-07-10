from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.forms import CursoFormulario


def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola Mundo {fecha_hora_ahora}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

def mostrar_index(Request):
    return render(Request, "mi_app/index.html", {"titulo": "Esta es la Primer Website de Fran"})

def formulario_curso(Request):
    if Request.method == "POST":
        pass
    else:
        mi_formulario = CursoFormulario()
        return render(Request, "mi_app/curso_formulario.html", {"mi_formulario": mi_formulario})
        