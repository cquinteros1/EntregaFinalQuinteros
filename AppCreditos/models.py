from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CRE(models.Model):
    
    def __str__(self):
        return f'Nombre: {self.nombre} / Apellido: {self.apellido} / DNI: {self.dni}'
    
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dni = models.IntegerField()
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    fecha_cred = models.DateField()
    importe = models.FloatField()
    cuotas = models.IntegerField()


class RES(models.Model):

    usuario = models.CharField(max_length=25)
    comercio_res = models.CharField(max_length=25)
    comentario = models.CharField(max_length=200)
    

class IMG(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    