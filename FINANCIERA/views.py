from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# PAGINA DE INCIO ---------------------------------------------------

def inicio(request):
    return render(request,'FINANCIERA/templates/inicio.html')

# ACERCA DE MI -----------------------------------------------------

def about(request):
    return render(request,'FINANCIERA/templates/about.html')

