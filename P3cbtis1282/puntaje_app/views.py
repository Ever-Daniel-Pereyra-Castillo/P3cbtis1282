from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")

def empleados(request):
    return render(request,"empleado.html")

def productos(request):
    return render(request,"productos.html")

def ventas(request):
    return render(request,"ventas.html")

def clientes(request):
    return render(request,"clientes.html")

def sucursales(request):
    return render(request,"sucursales.html")

def contactos(request):
    return render(request,"contactos.html")

