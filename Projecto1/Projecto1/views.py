import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): # primera vista

    p1=Persona("Emilio","Ramon")
    ahora=datetime.datetime.now()
    temasDelCurso=["Plantillas","Modelos","Formularios","Vistas", "Despliegues"]
    
    #temasDelCurso=[]
    #doc_externo=open("C:/Users/soporte/Documents/Proyectos Django/Projecto1/Projecto1/Platillas/Hola.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    
    doc_externo=get_template('Hola.html')
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})
   
    #documento=plt.render(ctx)
    documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})
   
    return HttpResponse(documento)

def despedida(request):

    doc_externo=open("C:/Users/soporte/Documents/Proyectos Django/Projecto1/Projecto1/Platillas/Chau.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)

    return HttpResponse(documento)

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    fecha="""<html>
            <body>
            <h1>
            Fecha y hora actuales: %s
            </h1>
            </body>
            </html>""" % fecha_actual
    return HttpResponse(fecha)

def calculaEdad(request, edad, agno):
    
    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno,edadFutura)

    return HttpResponse(documento)
