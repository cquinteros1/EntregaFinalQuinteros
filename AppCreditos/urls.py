from django.urls import path, include
from AppCreditos.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
        path('iniCli/', iniCliente, name="INI_CLI"),
        path('altaCred/', cred, name="CREDS"), 
        path('altaResena/', rese, name="RESENA"), 
        path('busqCrRe/', busquedaResena, name="BUSQ_CR_RE"),
        path('resultCrRe/', resultadosResena, name="RES_CR_RE"),
        path('login/', login_usuario, name="LOGIN"), 
        path('registro/', registro_usuario, name="REGISTRO"),
        path('logout/', LogoutView.as_view(template_name='AppCreditos/logout.html'), name="LOGOUT"),
        path('editarUser/', editar_usuario, name="EDIT_USR"),
        path('altaAvatar/', agregarAvatar, name="AVATAR"),
]

