import random
import string

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class AdministradorUsuarios(BaseUserManager):
    def create_user(self, correo, primer_nombre, apellido, password, **other_fields):

        if not correo:
            raise ValueError(_('Debes ingresar un email valido'))

        correo = self.normalize_email(correo)
        user = self.model(correo=correo, primer_nombre=primer_nombre,
                          apellido=apellido, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, correo, primer_nombre, apellido, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Super usuario debe debe tener valor is_staff "True"')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Super usuario debe debe tener valor is_superuser "True"')

        return self.create_user(correo, primer_nombre, apellido, password, **other_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(_('dirección de correo'), unique=True)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    imagen_perfil = models.ImageField(
        upload_to='usuarios/', default='usuarios/predeterminada.jpg')

    slug = models.SlugField(max_length=255, unique=True)

    fecha_registro = models.DateTimeField(default=timezone.now)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['primer_nombre', 'apellido']
    objects = AdministradorUsuarios()

    def __str__(self):
        return f'{self.primer_nombre} {self.apellido}'

    def get_absolute_url(self):
        return reverse('usuarios:usuario_detalle', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.correo)
        super(Usuario, self).save(*args, **kwargs)
