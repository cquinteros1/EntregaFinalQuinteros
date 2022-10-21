from django.db import models

# Create your models here.

class COM(models.Model):
    
    def __str__(self):
        return f'Nombre: {self.nombre} / Rubro: {self.rubro} / Direccion: {self.direccion} / Ciudad: {self.ciudad}'

    nombre = models.CharField(max_length=25)
    cuit = models.IntegerField()
    rubro = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)
    provincia = models.CharField(max_length=25)
    fecha_adhesion = models.DateField()