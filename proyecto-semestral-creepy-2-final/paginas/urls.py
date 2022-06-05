from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('historias/<slug:idcreepypasta>', historias, name="historias"),
    path('informacion/', informacion, name="informacion"),
    path('logueate/', logueate, name="logueate"),
    path('listadom/', listadom, name="listadom"),
    path('registro/', registro, name="registro"),
    path('subircreepy/', subircreepy, name="subircreepy"),
    path('tushistorias/', tushistorias, name="tushistorias"),
    path('vermensajesadmi/', vermensajesadmi, name="vermensajesadmi"),
    path('enviarmensajeadmi/', enviarmensajeadmi, name="enviarmensajeadmi"),
    path('registraM/', registraM, name="registraM"),
    path('registraMEN/', registraMEN, name="registraMEN"),
    path('eliminarcreepy/<codigos>', eliminarcreepy, name="eliminarcreepy"),
    path('borrarmensajes/<id>', borrarmensajes, name="borrarmensajes"),
     path('borrarusuario/<ide>', borrarusuario, name="borrarusuario"),

    path('usuario/<usuario>', cargar_usuario, name='cargar_usuario'),
    path('megusta/<idcreepypasta>', añadir_megusta, name='añadir_megusta'),
    path('agregar_comentario/<idcreepypasta>', agregar_comentario, name='agregar_comentario'),
    path('verusuariosadmi/', verusuariosadmi, name="verusuariosadmi"),
    path('ajustedatos/<ides>', ajustedatos, name="ajustedatos"),


     


]
