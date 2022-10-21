from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCreditos.models import IMG

# FORMULARIO SOLICITUD CREDITO --------------------------------------------------

class CredForm(forms.Form):
    nombre_F = forms.CharField(label='Nombre', max_length=25)
    apellido_F = forms.CharField(label='Apellido',max_length=25)
    dni_F = forms.IntegerField(label='DNI')
    fecha_nac_F = forms.DateField(label='Fecha Nacimiento(aaaa-mm-dd)')
    telefono_F = forms.IntegerField(label='Telefono')
    fecha_cred_F = forms.DateField(label='Fecha Credito(aaaa-mm-dd)')
    importe_F = forms.FloatField(label='Importe')
    cuotas_F = forms.IntegerField(label='Cuotas')


# FORMULARIO RESEÑA -------------------------------------------------------------

class ReseForm(forms.Form):
    usuario_F = forms.CharField(label='Usuario', max_length=25)
    comercio_res_F = forms.CharField(label='Comercio', max_length=25)
    comentario_F = forms.CharField(label='Comentario', max_length=200)
    

# FORMULARIO REGISTRO -----------------------------------------------------------

class RegForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_texts = {'username': None} # saca el texto auxiliar de usuario
        
        
# FORMULARIO EDITAR USUARIO -----------------------------------------------------

class EditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']    


# FORMULARIO AVATAR --------------------------------------------------------------

class AvaForm(forms.ModelForm):
    
    class Meta:
        model = IMG
        fields = ['imagen']