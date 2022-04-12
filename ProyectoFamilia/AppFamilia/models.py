from django.db import models

# Create your models here.

class Miembro(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    edad = models.IntegerField()
    relacion = models.CharField('relacion', max_length=50)
    mail = models.CharField('mail', max_length=50)