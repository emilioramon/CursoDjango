import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request): # primera vista

    doc_externo=open("C:/Users/soporte/Documents/Proyectos Django/Projecto1/Projecto1/Platillas/Hola.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    
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
