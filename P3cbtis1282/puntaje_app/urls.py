from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("sucursales/",views.sucursales,name="sucursales"),
    path("clientes/",views.clientes,name="clientes"),
    path("ventas/",views.ventas,name="ventas"),
    path("empleados/",views.empleados,name="empleados"),
    path("productos/",views.productos,name="productos"),
    path("contactos/",views.contactos,name="contactos"),
]

