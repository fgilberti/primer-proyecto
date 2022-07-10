from django.shortcuts import render


def mostrar_home(Request):
    return render(Request, "manejador_contenido/home.html", {})


def mostrar_profile(Request):
    return render(Request, "manejador_contenido/profile.html", {})
