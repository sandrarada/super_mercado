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
def agregarCarro(request, idProd):
    idProd = int(idProd)
    regUsuario = request.user
    msj = None
    #leer reg del producto en Producto
    existe = Producto.objects.filter(id=idProd).exists()
    if existe:
        regProducto = Producto.objects.get(id=idProd)
        # si no existe en carrito:
        existe = Carro.objects.filter(producto=regProducto, estado= 'activo', usuario= 
        regUsuario).exists()
        if existe:
            # instanciar un objeto de la clase Carrito
            regCarro = Carro.objects.get(producto=regProducto, estado= 'activo', usuario= regUsuario)
            #incrementar cantidad
            regCarro.cantidad += 1
        else:
            regCarro = Carro(producto=regProducto, usuario= regUsuario, valUnit = regProducto.precioUnitario)
            # guardar el registro
            regCarro.save()
    else: 
        # dar mensaje
        msj = 'Producto no disponible'
        # redireccionar a 'verProducto'
    return verProducto(request, idProd, msj) 
def verCarrito(request):
    context = consultarCarro(request)
    return render(request, 'productos/carrito.html', context)
def eliminarCarrito(request, id):
    #Consultar el reg y cambiar estado
    regCarrito = Carro.objects.get(id=id)
    regCarrito.estado = 'anulado'
    #guardar en BD
    regCarrito.save()
    #Desplegar el carrito
    return verCarrito(request)

def cambiarCantidad(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            #Toma la data enviada por el cliente
            data = json.load(request)
            id = data.get('id')
            cantidad = int(data.get('cantidad'))
            if cantidad > 0:
                #Lee el registro y lo modifica
                regProducto = Carro.objects.get(id=id)
                regProducto.cantidad = cantidad
                regProducto.save()
                context = consultarCarro(request)
                return JsonResponse(context)
            return JsonResponse({'alarma': 'no se pudo modificar...'}, status=400)
        else:
            return verCarrito(request)
