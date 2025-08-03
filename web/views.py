from django.shortcuts import render
from .models import Proyecto

def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html')

def contact(request):
    return render(request, 'web/contact.html')

def proyectos(request):
    lista_proyectos = Proyecto.objects.all()
    return render(request, 'web/proyectos.html',{'proyectos': lista_proyectos})