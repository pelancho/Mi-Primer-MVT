from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader

def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendi! esto es super facil")

def diaDeHoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)


def saludo_con_nombre(self, nombre):
    
    return HttpResponse("<h1>Hola mi nombre es: " +nombre+ "<h1>")


def calculaAñoNacimiento(self, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")


def probandoHtml(self):
    
    
    nom = "Ilan"
    ape=  "Chocron"
    lista_de_notas=[9,5,3,8,7,1,9,3,8 ]
    
    diccionario={'nombre':nom, 'apellido':ape,'lista':lista_de_notas}

    plantilla =loader.get_template('template1.html')
    
    documento=plantilla.render(diccionario)
   
    return HttpResponse(documento)


def comidasfavoritas(self):
    lista_de_comidas=['Sushi','Asado','Milanesa','Empanadas','Pizza']
    diccionario={'listaC':lista_de_comidas}
    plantillaC =loader.get_template('template1.html')
    
    documento=plantillaC.render(lista_de_comidas)
   
    return HttpResponse(documento)


def probandonumerosHTML(self):
    
    lista_de_notitas=[7,9,2,4,1,2,3 ]
    
    diccionarioN={'listanotas':lista_de_notitas}

    plantilla =loader.get_template('template1.html')
    
    documento=plantilla.render(diccionarioN)
   
    return HttpResponse(documento)
