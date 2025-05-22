from django.shortcuts import render, redirect
from .models import Museo, Etnomusicologo, Intervencion
from django.contrib import messages

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

#Guardar los datos

def guardarMuseo(request):
    Museo.objects.create(
        nombre=request.POST["nombre"],
        pais=request.POST["pais"],
        ciudad=request.POST["ciudad"],
        direccion=request.POST["direccion"],
        fundado_en=request.POST["fundado_en"]
    )
    messages.success(request, "MUSEO GUARDADO EXITOSAMENTE")
    return redirect('/museos')

def guardarEtnomusicologo(request):
    Etnomusicologo.objects.create(
        codigo_trabajador=request.POST["codigo_trabajador"],
        nombre=request.POST["nombre"],
        especialidad=request.POST["especialidad"],
        email=request.POST["email"],
        telefono=request.POST["telefono"]
    )
    messages.success(request, "ETNOMUSICOLOGO GUARDADO EXITOSAMENTE")
    return redirect('/etnomusicologos')


def guardarIntervencion(request):
    etno = Etnomusicologo.objects.get(id=request.POST["etnomusicologo"])
    museo = Museo.objects.get(id=request.POST["museo"])
    Intervencion.objects.create(
        etnomusicologo=etno,
        museo=museo,
        descripcion=request.POST["descripcion"],
        fecha=request.POST["fecha"],
        duracion_dias=request.POST["duracion_dias"]
    )
    messages.success(request, "INTERVENCIÓN GUARDADA EXITOSAMENTE")
    return redirect('/intervenciones')

#Eliminar

def eliminarMuseo(request, id):
    Museo.objects.get(id=id).delete()
    return redirect('/museos')

def eliminarEtnomusicologo(request, id):
    Etnomusicologo.objects.get(id=id).delete()
    return redirect('/etnomusicologos')

def eliminarIntervencion(request, id):
    Intervencion.objects.get(id=id).delete()
    return redirect('/intervenciones')

#Editar 
def editarMuseo(request, id):
    museo = Museo.objects.get(id=id)
    return render(request, "editarMuseo.html", {'museo': museo})

def editarEtnomusicologo(request, id):
    etno = Etnomusicologo.objects.get(id=id)
    return render(request, "editarEtnomusicologo.html", {'etno': etno})

def editarIntervencion(request, id):
    intervencion = Intervencion.objects.get(id=id)
    museos = Museo.objects.all()
    etnos = Etnomusicologo.objects.all()
    return render(request, "editarIntervencion.html", {
        'intervencion': intervencion,
        'museos': museos,
        'etnos': etnos
    })

#Actualizar

def actualizarMuseo(request):
    museo = Museo.objects.get(id=request.POST["id"])
    museo.nombre = request.POST["nombre"]
    museo.pais = request.POST["pais"]
    museo.ciudad = request.POST["ciudad"]
    museo.direccion = request.POST["direccion"]
    museo.fundado_en = request.POST["fundado_en"]
    museo.save()
    messages.success(request, "MUSEO ACTUALIZADO EXITOSAMENTE")
    return redirect('/museos')

def actualizarEtnomusicologo(request):
    etno = Etnomusicologo.objects.get(id=request.POST["id"])
    etno.codigo_trabajador = request.POST["codigo_trabajador"]
    etno.nombre = request.POST["nombre"]
    etno.especialidad = request.POST["especialidad"]
    etno.email = request.POST["email"]
    etno.telefono = request.POST["telefono"]
    etno.save()
    messages.success(request, "ETNOMUSICOLOGO ACTUALIZADO EXITOSAMENTE")
    return redirect('/etnomusicologos')

def actualizarIntervencion(request):
    intervencion = Intervencion.objects.get(id=request.POST["id"])
    intervencion.etnomusicologo = Etnomusicologo.objects.get(id=request.POST["etnomusicologo"])
    intervencion.museo = Museo.objects.get(id=request.POST["museo"])
    intervencion.descripcion = request.POST["descripcion"]
    intervencion.fecha = request.POST["fecha"]
    intervencion.duracion_dias = request.POST["duracion_dias"]
    intervencion.save()
    messages.success(request, "INTERVENCIÓN ACTUALIZADA EXITOSAMENTE")
    return redirect('/intervenciones')
