import datetime
import re
from django.http import HttpResponse

hola="""<html>
<body>
<h1>
Hola como te va, primera pagina con Django
</h1>
</body>
</html>"""
chau="""<html>
<body>
<h1>
Hasta luego
</h1>
</body>
</html>"""

def saludo(request): # primera vista

    return HttpResponse(hola)

def despedida(request):

    return HttpResponse(chau)

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
