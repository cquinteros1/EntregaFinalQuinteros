from django.urls import path, include
from AppComercios.views import *

urlpatterns = [
    path('iniCom/', iniComercio, name="INI_COMER"),
    path('busqCoRu/', busquedaRubro, name="BUSQ_CO_RU"),
    path('resultCoRU/', resultadosRubro, name="RES_CO_RU"),
    
    # CRUD Comercios
    path('altaCom/', comer, name="COMER"),
    path('comerciosVer/', verComercios, name="VER_COM"),
    path('comercioEliminar/<nombreCom>/', eliminarComercios, name="ELI_COM"),
    path('comercioEditar/<nombreCom>/', editarComercios, name="EDI_COM"),    
]