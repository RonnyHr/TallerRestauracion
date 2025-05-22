from django.urls import path
from .import views 

urlpatterns = [
    # RUTAS PARA MUSEO
    path('museos', views.listaMuseos),
    path('nuevoMuseo', views.nuevoMuseo),
    path('guardarMuseo', views.guardarMuseo),
    path('eliminarMuseo/<int:id>', views.eliminarMuseo),
    path('editarMuseo/<int:id>', views.editarMuseo),
    path('actualizarMuseo', views.actualizarMuseo),

    # RUTAS PARA ETNOMUSICOLOGO
    path('etnomusicologos', views.listaEtnomusicologos),
    path('nuevoEtnomusicologo', views.nuevoEtnomusicologo),
    path('guardarEtnomusicologo', views.guardarEtnomusicologo),
    path('eliminarEtnomusicologo/<int:id>', views.eliminarEtnomusicologo),
    path('editarEtnomusicologo/<int:id>', views.editarEtnomusicologo),
    path('actualizarEtnomusicologo', views.actualizarEtnomusicologo),
]