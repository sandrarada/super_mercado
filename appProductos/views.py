from django.shortcuts import render
from .models import *
# Create your views here.
def verCategorias(request):
    #Consultar categorias
    listaCateg = Categoria.objects.all()
    #ensamblar context
    context = {
        'categorias': listaCateg,
        'titulo': 'Categorias de Productos del Supermercado',
    }
    #renderizar
    return render(request, 'productos/categorias.html', context)
def verProductosCategoria(request, idCategoria):
    #Consultar categorias
    idCat = int(idCategoria)
    nombreCat = Categoria.objects.get(id=idCat)
    listaProductos = Producto.objects.filter(categoria= idCat)
    #ensamblar context
    context = {
    'productos': listaProductos,
    'titulo': 'Productos de la categoria ' + str(nombreCat),
    }
    #renderizar
    return render(request, 'productos/productos.html', context)
def verProducto(request, idProd, msj = None):
    #Consultar
    idProd = int(idProd)
    regProducto = Producto.objects.get(id= idProd)
    #ensamblar context
    context = {
        'producto': regProducto,
        'titulo': 'Detalles de ' + str(regProducto.nombre),
    }
    if msj:
        context['mensaje']= msj
    #renderizar
    return render(request, 'productos/producto.html', context)