from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from usuarios.models import Usuario
from usuarios.forms import usuariosForm , comentarioForm

from .models import Comentario, CreepyPasta, Genero, MensajesAdmi2


def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required(login_url='logueate')
def ajustedatos(request,ides):
    datos1 = Usuario.objects.get(correo = ides)
    datos = {
        'form': usuariosForm(instance=datos1)
    }
    if request.method== 'POST':
        formulario = usuariosForm(data=request.POST,instance=datos1)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="tushistorias")

    return render(request, 'paginas/ajustecuenta.html',datos)


@login_required(login_url='logueate')
def ajustescomentarios(request,ideees):
    datos2 = Comentario.objects.get(idcomentario = ideees)
    datos = {
        'form1': comentarioForm(instance=datos2)
    }
    if request.method== 'POST':
        formulario = comentarioForm(data=request.POST,instance=datos2)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="inicio")

    return render(request, 'paginas/ajustecomentarios.html',datos)




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
def borrarcomentarios(request, idees):

    borrarUS = Comentario.objects.get(idcomentario=idees)
    borrarUS.delete()

    return redirect(to="inicio")



@permission_required('is_staff', login_url="inicio")
def listadom(request):
    creepypasta1 = CreepyPasta.objects.all()
    contexto = {"lista": creepypasta1}
    return render(request, 'paginas/menuadmi.html', contexto)

@login_required(login_url='logueate')
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


 #esto es un recorador para hacer una vista privada que requiera login
@login_required(login_url='logueate')
def tushistorias(request):
    #para que solo se vean los creepi del usuario logueado pongo el filter (creador = reqyet.user)
    
    tushistorias1 = CreepyPasta.objects.filter(creador = request.user)
    contexto = {"listos": tushistorias1}
    return render(request, 'paginas/tuscreepy.html', contexto)

@permission_required('is_staff', login_url="inicio")
def verusuariosadmi(request):
    usuariomenu = Usuario.objects.all()
    contexto = {"listas2": usuariomenu}
    return render(request, 'paginas/usuariomenuadmi.html', contexto)



@permission_required('is_staff', login_url="inicio")
def vermensajesadmi(request):
    mensajes = MensajesAdmi2.objects.all()
    contexto = {"listas": mensajes}
    return render(request, 'paginas/vermensajesadmi.html', contexto)



@login_required(login_url='logueate')
def enviarmensajeadmi(request):
    return render(request, 'paginas/veryenviarmensajesaadmi.html')


def registraMEN(request):
    mensajes3 = request.POST['mensajecreepy']
    usuario = request.user
    consulta3 = request.POST['motivocreepycrear']
    #esto agrega el usuario al objeto creado
    MensajesAdmi2.objects.create(mensaje=mensajes3, consultasadmi=consulta3, usuario = usuario)

    return redirect('enviarmensajeadmi')


def eliminarcreepy(request, codigos):

    borrar = CreepyPasta.objects.get(idcreepypasta=codigos)
    borrar.delete()

    return redirect(to="listadom")

def eliminarcreepy1(request, codigos1):

    borrar = CreepyPasta.objects.get(idcreepypasta=codigos1)
    borrar.delete()

    return redirect(to="tushistorias")


def borrarusuario(request, ide):

    borrarUS = Usuario.objects.get(correo=ide)
    borrarUS.delete()

    return redirect(to="verusuariosadmi")



    


def borrarmensajes(request, id):
    borrarmensaje = MensajesAdmi2.objects.get(idmensaje=id)
    borrarmensaje.delete()
    return redirect(to="vermensajesadmi")


@login_required(login_url='logueate')
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
