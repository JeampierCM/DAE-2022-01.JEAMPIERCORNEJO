from django.urls import path

from . import views
app_name = 'encuesta'

urlpatterns =[
    path('volumen',views.volumen, name='volumen'),
    path('cilindro',views.vol, name='vol'),
    path('calcular',views.calcular, name='calcular'),
    path('matematica',views.mate, name='mate'),
    path('enviar',views.enviar, name='enviar'),
    path('',views.index, name='index'),
]
