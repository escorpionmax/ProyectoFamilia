from django.urls import path

from .views import Persona

urlpatterns = [
    path('agregar-miembro/<nombre>/<edad>/<relacion>/<mail>/', Persona)
]
