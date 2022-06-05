from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]
