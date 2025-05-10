from django.shortcuts import render, get_object_or_404 
# importamos el render, realiza el html
# y coloca las variables que le pasamos. El get_object_or_404 es para obtener un objeto o 
# devolver un 404 si no existe.
from .models import Estudiante, Profesor, Entregable, Curso
def index(request):
    return render(request, 'AppCoder/index.html')
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all() #trae todos los estudiantes de la base de datos
    # y los guarda en la variable estudiantes. El objects.all() es un método de Django 
    # que trae todos los objetos de una tabla
    contexto = {'estudiantes': estudiantes} #creamos un diccionario con la variable estudiantes
    # y la pasamos al template.
    return render(request, 'AppCoder/estudiantes.html', contexto)

def detalle_estudiante(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=pk) #busca el estudiante por pk, 
    # si no lo encuentra devuelve 404. Donde el pk es el id del estudiante.
    return render(request, 'AppCoder/estudiantes_detail.html', {'estudiante': estudiante})
def lista_profesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores de la base de datos
    # y los guarda en la variable profesores. El objects.all() es un método de Django 
    # que trae todos los objetos de una tabla
    contexto = {'profesores': profesores} #creamos un diccionario con la variable profesores
    # y la pasamos al template.
    return render(request, 'AppCoder/profesores.html', contexto)
# Create your views here.
