from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app(request):
    return HttpResponse("Desde la vista de matematicas!")

def sumar(request):
    return HttpResponse("Comensemos a Sumar")

def Rsuma(request, primer,segundo):
    sumita = primer + segundo
    return HttpResponse("La Suma de %s + %s = %s." %(primer, segundo,sumita))

def restar(request):
    return HttpResponse("Comensemos a Restar")

def Rresta(request, primer, segundo):
    restita = primer - segundo
    return HttpResponse("La Resta de %s - %s = %s." %(primer, segundo, restita))

def multiplicar(request):
    return HttpResponse("Comensemos a Multiplicar")

def Rmultiplica(request, primer, segundo):
    multi = primer * segundo
    return HttpResponse("La Multiplicacion de %s * %s = %s." %(primer, segundo, multi))