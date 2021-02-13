from django.http import HttpResponse
from django.shortcuts import render #HttpResponse
import datetime
from django.template import Template, Context,loader

class Persona(object):
    def __init__(self, segundo_nombre, apellido):
        self.segundo_nombre = segundo_nombre
        self.apellido = apellido
def index (request):
    return render (request, 'index.html')

def saludo(request):
    return HttpResponse("Hola Mundo, esta es mi primera página con Django")

def saludo2(request):
    nombre = "Juan"
    fecha = datetime.datetime.now()
    persona1 = Persona("Andres", "Alvarez")
    temas_del_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    otros_temas = []
#    doc_externo = open ("C:/Python_stack/django/Proyectos_Django/Proyecto1/Proyecto1/templates/plantilla1.html")
#    plt = Template(doc_externo.read())
#    doc_externo.close()
#    ctx = Context({"nombre_persona": nombre, "apellido_persona": "Alvarez", "fecha": fecha,
 #                   "segundo_nombre": persona1.segundo_nombre,
 #                   "temas": ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"],
 #                   "temas2": temas_del_curso,
 #                   "otros_temas": otros_temas,})
#    documento = plt.render(ctx)

    doc_externo= loader.get_template('plantilla1.html')
    documento = doc_externo.render({"nombre_persona": nombre, "apellido_persona": "Alvarez", "fecha": fecha,
                    "segundo_nombre": persona1.segundo_nombre,
                    "temas": ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"],
                    "temas2": temas_del_curso,
                    "otros_temas": otros_temas,})
    return HttpResponse(documento)
    #o podriamos usar render: nos ahorramos las lineas doc_externo = loader...,
    #documento = doc_externo.render... 
    #return = render(request, 'plantilla1.html', context) -> podriamos pasar
    # el diccionario directo en el contexto

def despedida (request):
    return HttpResponse("Hasta luego Mundo")

def fecha (request):
    fecha_actual=datetime.datetime.now()
    documento = "<html><body><h1>Fecha y Hora actual: %s </h1></body></html>" %fecha_actual
    return HttpResponse(documento)

def calcula_edad (request,edad,year):
    periodo = year - 2020
    edad_futura = edad+periodo
    documento = "<html><body><h2> En el año %s tendrás %s años</h2></body></html>" %(year, edad_futura)
    return HttpResponse(documento)

def herencia_plantilla (request):
    fecha = datetime.datetime.now()
    return render(request, "plantillaHija.html", {"fecha": fecha})

def herencia_plantilla2 (request):
    fecha = datetime.datetime.now()
    return render(request, "plantillaHija2.html", {"fecha": fecha})

    