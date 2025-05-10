from django.contrib import admin
from .models import Estudiante, Profesor, Entregable, Curso
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Curso)
# Register your models here.
