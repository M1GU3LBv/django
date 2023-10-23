from django.contrib import admin
from .models import Persona

# Register your models here.

admin.site.register(Persona)
admin.site.site_header = 'Administración de Personas'

