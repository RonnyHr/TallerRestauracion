from django.contrib import admin
from .models import Museo
from .models import Etnomusicologo
from .models import Intervencion

# Register your models here.
admin.site.register(Museo)
admin.site.register(Etnomusicologo)
admin.site.register(Intervencion)