from django.shortcuts import render
from .models import *

# Create your views here.
def libro(response):
    libros = Libro.objects.all()
    prestamos = Prestamos.objects.all()
    usuario = Usuario.objects.all()

    return render(response, 'libro/libro.html', {'libros': libros, 'prestamos':prestamos, 'usuario':usuario})