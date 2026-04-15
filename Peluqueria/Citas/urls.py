from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('registro/', views.Registro, name='registro'),
    path('index/', views.index, name='index'),
    path('cita/', views.listarCitas, name='cita'),
    path('cita/agregar/', views.agregarCita, name='agregarCita'),
    path('cita/editar/<int:id>/', views.editarCita, name='editarCita'),
    path('cita/eliminar/<int:id>/', views.eliminarCita, name='eliminarCita'),
    path('profesional/crearpro/', views.agregarProfesional, name='agregarProfesional'),
    path('obtener-profesionales/', views.obtener_profesionales, name='obtener_profesionales'),
    path('servicio/crearser/', views.agregarServicio, name='agregarServicio'),
]
