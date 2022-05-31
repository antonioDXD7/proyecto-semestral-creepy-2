import email
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.hashers import make_password
from .models import Usuario

# Create your views here.
def registrar(request):
    imagen = request.FILES['imagenperfil']
    nombre = request.POST["nombreregistro"]
    apellido = request.POST["apellidoregistro"]
    correo = request.POST["correoregistro"]
    contraseña = request.POST["confirmarcontraseñaregistro"]
    get_user_model().objects.create(correo=correo, primer_nombre=nombre, apellido=apellido, imagen_perfil=imagen, password=make_password(contraseña))
    return redirect(to='logueate')

def iniciar(request):
    correo = request.GET["correorelogin"]
    contraseña = request.GET["contraseñalogin"]
    usuario = authenticate(request, correo=correo, password=contraseña)
    if usuario is not None:
        login(request, usuario)
        return redirect(to='inicio')
    return redirect(to="logueate")

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')