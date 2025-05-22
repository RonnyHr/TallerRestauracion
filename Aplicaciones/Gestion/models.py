from django.db import models

# Create your models here.

# Museo
class Museo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField()
    fundado_en = models.PositiveIntegerField()

    def _str_(self):
        return f"{self.nombre} ({self.pais})"
    
# Etnomusicologo 
class Etnomusicologo(models.Model):
    codigo_trabajador = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.nombre} - {self.codigo_trabajador}"
    

#Intervencion
    
class Intervencion(models.Model):
    etnomusicologo = models.ForeignKey(Etnomusicologo, on_delete=models.CASCADE, related_name='intervenciones')
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name='intervenciones')
    descripcion = models.TextField()
    fecha = models.DateField()
    duracion_dias = models.PositiveIntegerField()

    def _str_(self):
        return f"{self.etnomusicologo.nombre} → {self.museo.nombre} ({self.fecha})"