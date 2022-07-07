import email
from tkinter import E, N
from django.db import models
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision =models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email =models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email =models.EmailField()
    profesion = models.CharField(max_length=50)

class entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad= models.IntegerField()
# Create your models here.

