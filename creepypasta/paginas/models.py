from django.db import models

# Create your models here.
class genero(models.Model):
    idgenero = models.AutoField(primary_key=True,verbose_name="ID autoincrementable del genero")
    genero = models.CharField(max_length=30, verbose_name="Genero del creepy")

    def __str__(self):
        return self.genero

class creepypasta(models.Model):
    idcreepypasta = models.AutoField(verbose_name="id del creepypasta", primary_key=True)
    resumen = models.TextField()
    nombrecreepy = models.CharField(verbose_name="Nombre del creepypasta", max_length=20)
    historia = models.TextField(verbose_name="")
    imagen = models.ImageField(upload_to="creepypastas")
    generos = models.ForeignKey(genero,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrecreepy

class mensajesadmi2(models.Model):
    idmensaje = models.AutoField(verbose_name="id del mensaje", primary_key=True)
    mensaje = models.TextField(verbose_name="Nmensaje del admi")
    consultasadmi = models.CharField(verbose_name="tipo consulta", max_length=20)

    def __str__(self):
        return self.mensaje
