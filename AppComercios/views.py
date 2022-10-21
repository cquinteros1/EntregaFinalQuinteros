from django.shortcuts import render
from django.http import HttpResponse
from AppComercios.models import *
from AppComercios.forms import ComerForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

# WEB INICIO COMERCIOS --------------------------------------------------------------------

def iniComercio(request):
    return render(request, 'AppComercios/comercios.html')


# CARGA DE COMERCIOS ----------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def comer(request):
    if request.method == 'POST':
        
        form_comercio = ComerForm(request.POST)
        
        if form_comercio.is_valid():
            
            infoCo = form_comercio.cleaned_data
            
            co = COM(
                nombre = infoCo['nombreCo_F'],
                cuit = infoCo['cuit_F'],
                rubro = infoCo['rubro_F'],
                direccion = infoCo['direccion_F'],
                ciudad = infoCo['ciudad_F'],
                provincia = infoCo['provincia_F'],
                fecha_adhesion = infoCo['fecha_adhesion_F'])
            
            co.save()
            
            return render(request,'AppComercios/altaComOk.html')
        
    else:
        
        form_comercio = ComerForm()
        
    return render(request,'AppComercios/altaComercio.html', {'formCo':form_comercio})



# BUSQUEDA DE COMERCIOS -------------------------------------------------------------------

def busquedaRubro(request):
    return render(request, 'AppComercios/busqRubro.html')



# RESULTADOS BUSQUEDA COMERCIOS -----------------------------------------------------------

def resultadosRubro(request):    
    if request.GET['rubro']:
        
        rubroBuscado = request.GET['rubro']
        com_por_rubros = COM.objects.filter(rubro__icontains=rubroBuscado)
        
        return render(request, 'AppComercios/resultadosCom.html', {"COM":com_por_rubros, "rubro":rubroBuscado})
    
    else:
        
        respuesta = "No enviaste datos"
    
    return render(request, 'AppComercios/sinDatosCom.html', {"rta":respuesta})
  
    

# VER COMERCIOS --------------------------------------------------------------------------

def verComercios(request):
    comVer = COM.objects.all()
    
    return render(request, 'AppComercios/verComer.html', {'co_ver':comVer})



# ELIMINAR COMERCIOS ---------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def eliminarComercios(request, nombreCom):
    comEli = COM.objects.get(nombre=nombreCom)
    comEli.delete()
    
    comVer = COM.objects.all()
    contexto = {'co_ver':comVer}
    
    return render(request, 'AppComercios/elimComOk.html', contexto) # 'AppComercios/verComer.html'


# EDITAR COMERCIOS -----------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def editarComercios(request, nombreCom):
    comEdi = COM.objects.get(nombre=nombreCom)
    
    if request.method == "POST": # dar click al boton editar
        
        form_comercio = ComerForm(request.POST)
        
        if form_comercio.is_valid():
            
            infoCo = form_comercio.cleaned_data
            
            comEdi.nombre = infoCo['nombreCo_F']
            comEdi.cuit = infoCo['cuit_F']
            comEdi.rubro = infoCo['rubro_F']
            comEdi.direccion = infoCo['direccion_F']
            comEdi.ciudad = infoCo['ciudad_F']
            comEdi.provincia = infoCo['provincia_F']
            comEdi.fecha_adhesion = infoCo['fecha_adhesion_F']
            
            comEdi.save()
            
            return render(request,'AppComercios/editComOk.html') # hacer nuevo html de confirmacion de edicion
        
    else:
        
        form_comercio = ComerForm(initial={
            'nombreCo_F':comEdi.nombre,
            'cuit_F':comEdi.cuit,
            'rubro_F':comEdi.rubro,
            'direccion_F':comEdi.direccion,
            'ciudad_F':comEdi.ciudad,
            'provincia_F':comEdi.provincia,
            'fecha_adhesion_F':comEdi.fecha_adhesion
        })
        
    return render(request,'AppComercios/editarComercio.html', {'formCo':form_comercio, 'nombreCo_F':nombreCom})        
