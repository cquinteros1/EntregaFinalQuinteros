from django import forms

class ComerForm(forms.Form):
    nombreCo_F = forms.CharField(label='Nombre', max_length=25)
    cuit_F = forms.IntegerField(label='CUIT')
    rubro_F = forms.CharField(label='Rubro', max_length=25)
    direccion_F = forms.CharField(label='Direccion', max_length=25)
    ciudad_F = forms.CharField(label='Ciudad', max_length=25)
    provincia_F = forms.CharField(label='Provincia', max_length=25)
    fecha_adhesion_F = forms.DateField(label='Fecha Adhesion(aaaa-mm-dd)')