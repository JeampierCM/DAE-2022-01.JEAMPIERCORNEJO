from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from tienda.carrito import Cart
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()

    dicCategorias = {}
    for cat in category_list:
        dicCategorias[cat.id] = {
            'id' : cat.id,
            'nombre' : cat.nombre
        }
    request.session['nombreTienda'] = 'TIENDA TECH'
    request.session['listado_categorias'] = dicCategorias

    context = {'product_list': product_list}
    return render(request, 'index.html',context)


def producto(request, product_id):
    producto = get_object_or_404(Producto, pk=product_id)
    context = {
        'producto': producto}
    return render(request, 'producto.html',context)

def productoPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    product_list = Producto.objects.filter(categoria = objCategoria)
    context = {
        'product_list':product_list
    }
    return render(request,'index.html',context)

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)

    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
