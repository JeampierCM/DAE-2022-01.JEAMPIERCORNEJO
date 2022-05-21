from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ProductosView(APIView):
    
    def get(self,request):
        dataproducto = Producto.objects.all()
        serProducto = ProductoSerializer(dataproducto,many=True)
        return Response(serProducto.data)

    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)

    
class ProductoView(APIView):
        
        def get(self,request,pk):
            dataproducto = Producto.objects.get(pk=pk)
            serProducto = ProductoSerializer(dataproducto)
            return Response(serProducto.data)
    
        def put(self,request,pk):
            dataproducto = Producto.objects.get(pk=pk)
            serProducto = ProductoSerializer(dataproducto,data=request.data)
            serProducto.is_valid(raise_exception=True)
            serProducto.save()
            return Response(serProducto.data)
    
        def delete(self,request,pk):
            dataproducto = Producto.objects.get(pk=pk)
            dataproducto.delete()
            return Response(status=204)