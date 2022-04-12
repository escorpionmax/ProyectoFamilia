from django.http import HttpResponse
from django.shortcuts import render

from .models import Miembro

# Create your views here.

def Persona(request, nombre, edad, relacion, mail):
    miembro = Miembro(nombre, edad, relacion, mail)

    return HttpResponse(f'Se agregó a {miembro.nombre} como {miembro.relacion}')

