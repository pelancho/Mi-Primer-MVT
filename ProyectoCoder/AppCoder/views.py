from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

from AppCoder.models import Familiar
# Create your views here.


def curso(self):

    curso = Curso(nombre="Django", comision = 1570)
    curso.save()
    texto= f"Curso Creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)


def familiar(self):

    familiar = Familiar(nombre="Sergio", apellido = "Chocron",edad=63)
    familiar2 = Familiar(nombre="Sandra", apellido = "Sincofsky",edad=62)
    familiar3 = Familiar(nombre="Ariel", apellido = "Chocron",edad=18)



    familiar.save()
    familiar2.save()
    texto= f"Familiar Creado: {familiar.nombre} {familiar.apellido} {familiar.edad} |||| Familiar 2 Creado: {familiar2.nombre} {familiar2.apellido} {familiar2.edad} |||| Familiar 3 Creado: {familiar3.nombre}, {familiar3.apellido}, {familiar3.edad}"

    
    return HttpResponse(texto)