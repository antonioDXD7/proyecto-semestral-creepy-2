from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from usuarios.models import Usuario

from .models import Comentario, CreepyPasta, Genero, MensajesAdmi2


def inicio(request):
    return render(request, 'paginas/inicio.html')


def ajustedatos(request):
    return render(request, 'paginas/ajustecuenta.html')


def ajustecontrasenia(request):
    return render(request, 'paginas/ajustecuentacontraseña.html')


def informacion(request):
    return render(request, 'paginas/informacion.html')


def logueate(request):
    return render(request, 'paginas/logueate.html')


def registro(request):
    return render(request, 'paginas/registrate.html')


def historias(request, idcreepypasta):
    creepy = get_object_or_404(CreepyPasta, idcreepypasta=idcreepypasta)
    return render(request, 'paginas/historia1.html', {'creepy': creepy})


@permission_required('is_staff', login_url="inicio")
def listadom(request):
    creepypasta1 = CreepyPasta.objects.all()
    contexto = {"lista": creepypasta1}
    return render(request, 'paginas/menuadmi.html', contexto)


def subircreepy(request):
    generos = Genero.objects.all()
    contexto = {"lista_r": generos}
    return render(request, 'paginas/subircreepy.html', contexto)


def registraM(request):
    imagen2 = request.FILES['imagencreepy']
    nombrec = request.POST['nombrecreepycrear']
    resumen1 = request.POST['resumencreepy']
    historia1 = request.POST['historiacreepy']
    genero2 = request.POST['seleccion1']
    genero3 = Genero.objects.get(idgenero=genero2)

    CreepyPasta.objects.create(imagen=imagen2, nombrecreepy=nombrec, creador=request.user,
                               resumen=resumen1, historia=historia1, generos=genero3)

    return redirect('subircreepy')


def inicio(request):
    inicios = CreepyPasta.objects.all()
    contexto = {"listo": inicios}
    return render(request, 'paginas/inicio.html', contexto)


def tushistorias(request):
    tushistorias1 = CreepyPasta.objects.all()
    contexto = {"listos": tushistorias1}
    return render(request, 'paginas/tuscreepy.html', contexto)


@permission_required('is_staff', login_url="inicio")
def vermensajesadmi(request):
    mensajes = MensajesAdmi2.objects.all()
    contexto = {"listas": mensajes}
    return render(request, 'paginas/vermensajesadmi.html', contexto)


def enviarmensajeadmi(request):
    return render(request, 'paginas/veryenviarmensajesaadmi.html')


def registraMEN(request):
    mensajes3 = request.POST['mensajecreepy']
    consulta3 = request.POST['motivocreepycrear']
    MensajesAdmi2.objects.create(mensaje=mensajes3, consultasadmi=consulta3)

    return redirect('enviarmensajeadmi')


def eliminarcreepy(request, codigos):

    borrar = CreepyPasta.objects.get(idcreepypasta=codigos)
    borrar.delete()

    return redirect(to="listadom")


def borrarmensajes(request, id):
    borrarmensaje = MensajesAdmi2.objects.get(idmensaje=id)
    borrarmensaje.delete()
    return redirect(to="vermensajesadmi")


def añadir_megusta(request, idcreepypasta):
    creepy = get_object_or_404(CreepyPasta, idcreepypasta=idcreepypasta)
    if request.user in creepy.me_gusta.all():
        creepy.me_gusta.remove(request.user)
    else:
        creepy.me_gusta.add(request.user)
    creepy.save()
    return redirect(to='inicio')


@login_required(login_url='logueate')
def agregar_comentario(request, idcreepypasta):
    usuario = request.user
    creepy = get_object_or_404(CreepyPasta, idcreepypasta=idcreepypasta)
    cuerpo = request.POST["comentario"]
    comentario = Comentario(creepy=creepy, usuario=usuario, cuerpo=cuerpo)
    comentario.save()
    return redirect('historias', idcreepypasta=idcreepypasta)


def cargar_usuario(request, usuario):
    usuario = get_object_or_404(Usuario, correo=usuario)
    creepys_usuairo = CreepyPasta.objects.filter(creador=usuario)
    contexto = {"usuario": usuario, "creepys": creepys_usuairo}
    return render(request, 'paginas/usuario.html', contexto)
