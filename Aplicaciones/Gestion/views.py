from django.shortcuts import render
from .models import Museo, Etnomusicologo, Intervencion

# Create your views here.

#listar las entidades
def listaMuseos(request):
    museos = Museo.objects.all()
    return render(request, "museo.html", {'museos': museos})

def listaEtnomusicologos(request):
     etnos = Etnomusicologo.objects.all()
     return render(request, "etnomusicologo.html", {'etnomusicologos': etnos})

def listaIntervenciones(request):
    intervenciones = Intervencion.objects.all()
    return render(request, "intervencion.html", {'intervenciones': intervenciones})