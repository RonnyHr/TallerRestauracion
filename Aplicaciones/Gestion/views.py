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

#formularios nuevos
def nuevoMuseo(request):
    return render(request, "agregarMuseo.html")

def nuevoEtnomusicologo(request):
    return render(request, "agregarEtnomusicologo.html")

def nuevaIntervencion(request):
    museos = Museo.objects.all()
    etnos = Etnomusicologo.objects.all()
    return render(request, "agregarIntervencion.html", {"museos": museos, "etnos": etnos})