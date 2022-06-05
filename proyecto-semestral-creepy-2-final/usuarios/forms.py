from dataclasses import fields
from django import forms
from usuarios.models import Usuario
#from paginas.models import Usuario

class usuariosForm(forms.ModelForm):

    primer_nombre = forms.CharField(min_length=3,max_length=9)
    apellido = forms.CharField(min_length=3,max_length=9)
    correo = forms.EmailField(min_length=14,max_length=30)

    class Meta:
        model = Usuario
        fields = ["primer_nombre","apellido","correo"]


