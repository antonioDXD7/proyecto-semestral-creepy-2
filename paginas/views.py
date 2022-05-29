from django.shortcuts import redirect, render
from .models import creepypasta, genero ,mensajesadmi2

# Create your views here.


def inicio(request):
    return render (request,'paginas/inicio.html')

def ajustedatos (request):
    return render (request,'paginas/ajustecuenta.html')    

def ajustecontrasenia (request):
    return render (request,'paginas/ajustecuentacontraseña.html')



def informacion (request):
    return render (request,'paginas/informacion.html')

def logueate (request):
    return render (request,'paginas/logueate.html')

def registro (request):
    return render (request,'paginas/registrate.html')


def historias (request):
    return render (request,'paginas/historia1.html')


def listadom(request):
    creepypasta1 = creepypasta.objects.all()
    contexto = {"lista": creepypasta1}
    return render (request,'paginas/menuadmi.html',contexto)


def subircreepy(request):
    generos = genero.objects.all()
    contexto = {"lista_r": generos}
    return render (request,'paginas/subircreepy.html',contexto)

def registraM(request):
    imagen2 = request.FILES['imagencreepy']
    nombrec = request.POST['nombrecreepycrear']
    resumen1 = request.POST['resumencreepy']
    historia1 = request.POST['historiacreepy']
    genero2 = request.POST['seleccion1']
    genero3 = genero.objects.get(idgenero = genero2)

    creepypasta.objects.create( imagen = imagen2, nombrecreepy = nombrec, resumen = resumen1, historia = historia1, generos = genero3)

    return redirect('subircreepy')

def inicio(request):
    inicios = creepypasta.objects.all()
    contexto = {"listo": inicios}
    return render (request,'paginas/inicio.html',contexto)

def tushistorias (request):
    tushistorias1 = creepypasta.objects.all()
    contexto = {"listos": tushistorias1}
    return render (request,'paginas/tuscreepy.html',contexto)


def vermensajesadmi (request):
    mensajes = mensajesadmi2.objects.all()
    contexto = {"listas": mensajes}
    return render (request,'paginas/vermensajesadmi.html',contexto)


def enviarmensajeadmi (request):
    return render (request,'paginas/veryenviarmensajesaadmi.html')



def registraMEN(request):
    mensajes3 = request.POST['mensajecreepy']
    consulta3 = request.POST['motivocreepycrear']
    mensajesadmi2.objects.create(  mensaje = mensajes3 ,consultasadmi = consulta3) 

    return redirect('enviarmensajeadmi')

def eliminarcreepy (request, codigos):

    borrar = creepypasta.objects.get(idcreepypasta=codigos)
    borrar.delete()

    return redirect (to="listadom")

def borrarmensajes (request, id):

    borrarmensaje = mensajesadmi2.objects.get(idmensaje=id)
    borrarmensaje.delete()

    return redirect (to="vermensajesadmi")
