from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del genero")
    genero = models.CharField(max_length=30, verbose_name="Genero del creepy")

    def __str__(self):
        return self.genero

class CreepyPasta(models.Model):
    idcreepypasta = models.AutoField(verbose_name="id del creepypasta", primary_key=True)
    resumen = models.TextField()
    nombrecreepy = models.CharField(verbose_name="Nombre del creepypasta", max_length=20)
    historia = models.TextField(verbose_name="Historia")
    imagen = models.ImageField(upload_to="creepypastas")
    generos = models.ForeignKey(Genero,on_delete=models.CASCADE)
    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paginas_historia', null=True
    )
    me_gusta = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    def __str__(self):
        return self.nombrecreepy
    
    def get_absolute_url(self):
        return reverse("historias", args=[str(self.idcreepypasta)])
    def agregar_megusta(self):
        return reverse("añadir_megusta", args=[str(self.idcreepypasta)])
    @property
    def obtener_comentarios(self):
        comentarios = Comentario.objects.filter(creepy=self)
        return comentarios

class MensajesAdmi2(models.Model):
    idmensaje = models.AutoField(verbose_name="id del mensaje", primary_key=True)
    mensaje = models.TextField(verbose_name="Nmensaje del admi")
    consultasadmi = models.CharField(verbose_name="tipo consulta", max_length=20)

    def __str__(self):
        return self.mensaje


class Comentario(models.Model):
    creepy = models.ForeignKey(CreepyPasta, on_delete=models.CASCADE, related_name='comentarios', null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario}-->{self.cuerpo}'
