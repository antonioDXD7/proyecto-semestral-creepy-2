"""Creepypastas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',inicio,name="inicio"),
    path('ajustedatos/',ajustedatos,name="ajustedatos"),
    path('ajustecontrasenia/',ajustecontrasenia,name="ajustecontrasenia"),
    path('historias/<slug:idcreepypasta>',historias,name="historias"),
    path('informacion/',informacion,name="informacion"),
    path('logueate/',logueate,name="logueate"),
    path('listadom/',listadom,name="listadom"),
    path('registro/',registro,name="registro"),
    path('subircreepy/',subircreepy,name="subircreepy"),
    path('tushistorias/',tushistorias,name="tushistorias"),
    path('vermensajesadmi/',vermensajesadmi,name="vermensajesadmi"),
    path('enviarmensajeadmi/',enviarmensajeadmi,name="enviarmensajeadmi"),
    path('registraM/',registraM,name="registraM"),
    path('registraMEN/',registraMEN,name="registraMEN"),
    path('eliminarcreepy/<codigos>',eliminarcreepy,name="eliminarcreepy"),
    path('borrarmensajes/<id>',borrarmensajes,name="borrarmensajes"),
    
    path('usuario/(?P<usuario>[-a-zA-Z0-9_]+)\\Z', cargar_usuario, name='cargar_usuario'),
    path('megusta/<slug:idcreepypasta>', añadir_megusta, name='añadir_megusta'),
    path('agregar_comentario/<slug:idcreepypasta>', agregar_comentario, name='agregar_comentario')
  
]
