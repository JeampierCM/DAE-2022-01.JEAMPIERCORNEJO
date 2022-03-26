import imp
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : 'formulario'
    }
    return render(request, 'encuesta/formulario.html',context)

def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'nombre': request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],

    }
    return render(request, 'encuesta/respuesta.html',context)

def mate(request):
    context = {
        'titulo' : 'Matematicas'
    }
    return render(request, 'mat/form.html',context)

def calcular(request):
        ope = request.POST['operacion']
        val1=float(request.POST['valor1'])
        val2=float(request.POST['valor2'])
        resultado=0
        if ope=="Suma":
            resultado=val1+val2
        elif ope=="Resta":
            resultado=val1-val2
        elif ope=="Multiplicacion":
            resultado=val1*val2
        elif ope=="Division":
            resultado=val1/val2

        context = {
            'titulo' : 'Resolucion',
            'valor1' : request.POST['valor1'], 
            'valor2' : request.POST['valor2'],
            'operacion':request.POST['operacion'],
            'resultado':resultado,
        }
        return render(request, 'mat/respuesta.html',context) 

def vol(request):
    context = {
        'titulo' : 'CALCULO DEL VOLUMEN DE UN CILINDRO'
    }
    return render(request, 'cal_cilindro/formu.html',context)

def volumen(request):
    diametro=float(request.POST['diametro'])
    altura=float(request.POST['altura'])
    radio = diametro/2
    area_base=3.1416*(radio**2)
    volumen=area_base*altura
    context = {
        'titulo': 'VOLUMEN',
        'diametro':request.POST['diametro'],
        'altura':request.POST['altura'],
        'volumen':volumen
    }
    return render(request, 'cal_cilindro/respuesta.html', context)

# Create your views here.
