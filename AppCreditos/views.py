from django.shortcuts import render
from django.http import HttpResponse
from AppCreditos.forms import *
from AppCreditos.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

# LOGIN -----------------------------------------------------------------

def login_usuario(request):
    if request.method == 'POST':
        
        formLogin = AuthenticationForm(request, data = request.POST)
        
        if formLogin.is_valid():
            usuario = formLogin.cleaned_data.get('username')
            clave = formLogin.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = clave)
            
            if user:
                login(request, user)
                
                return render(request, 'FINANCIERA/templates/inicio.html', {'mensaje':f'{user}'})
            
        else:
            
            return render(request, 'FINANCIERA/templates/inicio.html', {'mensaje':'DATOS INCORRECTOS'})
        
    else:
        
        formLogin = AuthenticationForm()
        
    return render(request, 'AppCreditos/login.html', {'form_login':formLogin})



# REGISTRO --------------------------------------------------------------------------

def registro_usuario(request):
    if request.method == 'POST':
        
        formRegistro = RegForm(request.POST)
        
        if formRegistro.is_valid():
            
            username = formRegistro.cleaned_data['username']
            formRegistro.save()
            return render(request,'FINANCIERA/templates/inicio.html', {'mensaje':'Usuario creado'})
        
    else:
        
        formRegistro = RegForm()
        
    return render(request,'AppCreditos/registro.html',{'form_registro':formRegistro})
                


# EDICION USUARIO ------------------------------------------------------------------------

@login_required
def editar_usuario(request):
    
    userEdit = request.user
    
    if request.method == "POST":
        
        formEditar = EditForm(request.POST)
        
        if formEditar.is_valid():
            
            infoUser = formEditar.cleaned_data
            
            userEdit.email = infoUser['email']
            userEdit.set_password(infoUser['password1'])
            userEdit.first_name = infoUser['first_name']
            userEdit.last_name = infoUser['last_name']
            
            userEdit.save()
            
            return render(request,'AppCreditos/editarUsuOk.html')
        
    else: 
        
        formEditar = EditForm(initial={
            'email':userEdit.email,
            'first_name':userEdit.first_name,
            'last_name':userEdit.last_name,
        })
        
    return render(request, 'AppCreditos/editarUsuario.html', {'form_editUser':formEditar,'usuarioEdit':userEdit})


# WEB INICIO COMERCIOS --------------------------------------------------------------------

def iniCliente(request):
    return render(request, 'AppCreditos/clientes.html')



# SOLICITUD CREDITOS -----------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def cred(request):
    if request.method == 'POST': # despues de dar click al boton Guardar
        
        form_credito = CredForm(request.POST)
        
        if form_credito.is_valid():
            
            infoCr = form_credito.cleaned_data
            
            cr = CRE(
                nombre = infoCr['nombre_F'],
                apellido = infoCr['apellido_F'],
                dni = infoCr['dni_F'],
                fecha_nac = infoCr['fecha_nac_F'],
                telefono = infoCr['telefono_F'],
                fecha_cred = infoCr['fecha_cred_F'],
                importe = infoCr['importe_F'],
                cuotas = infoCr['cuotas_F'])
            
            cr.save()
            
            return render(request,'AppCreditos/altaCredOk.html')
        
    else:
        
        form_credito = CredForm()
        
    return render(request,'AppCreditos/altaCreditos.html', {'formCr':form_credito})



# ALTA RESEÑA ----------------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def rese(request):
    if request.method == 'POST':
        form_resena = ReseForm(request.POST)

        if form_resena.is_valid():

            infoRe = form_resena.cleaned_data

            re = RES(
                usuario = infoRe['usuario_F'],
                comercio_res = infoRe['comercio_res_F'],
                comentario = infoRe['comentario_F'])
            
            re.save()

            return render(request,'AppCreditos/altaResOk.html')
    
    else:

        form_resena = ReseForm()

    return render(request,'AppCreditos/altaResena.html', {'formRe':form_resena})



# BUSQUEDA DE RESEÑAS -------------------------------------------------------------------

def busquedaResena(request):
    return render(request, 'AppCreditos/busqResena.html')

        

# RESULTADOS BUSQUEDA RESEÑAS -----------------------------------------------------------

def resultadosResena(request):    
    if request.GET['comercio_res']:
        
        resBuscada = request.GET['comercio_res']
        res_por_comer = RES.objects.filter(comercio_res__icontains=resBuscada)
        
        return render(request, 'AppCreditos/resultadosRes.html', {"RES":res_por_comer, "comercio_res":resBuscada})
    
    else:
        
        respuesta = "No enviaste datos"
    
    return render(request, 'AppCreditos/sinDatosRes.html', {"rta_res":respuesta})



# AGREGAR AVATARES ---------------------------------------------------------------------

@login_required(login_url='/AppCreditos/login/')
def agregarAvatar(request):
    if request.method == "POST":
        
        form_avatar = AvaForm(request.POST, request.FILES)
        
        if form_avatar.is_valid():
            
            usuarioActual = User.objects.get(username=request.user)
            
            img_avatar = IMG(usuario=usuarioActual, imagen=form_avatar.cleaned_data['imagen'])
            
            img_avatar.save()
            
            return render(request,'AppCreditos/altaAvaOk.html')
        
    else:
        
        form_avatar = AvaForm()
        
    return render(request, 'AppCreditos/altaAvatar.html', {'formAva':form_avatar})

