from django.urls import path

from . import views

urlpatterns = [
    # ex: http://localhost:8000/app/
    path('', views.app, name='app'),

    #ex: http://localhost:8000/app/suma/
    path('suma/', views.sumar, name='suma'),

   # ex: http://localhost:8000/app/suma/18/19/
    path('suma/<int:primer>/<int:segundo>/', views.Rsuma, name='Rsum'),

    # ex: http://localhost:8000/app/resta/
    path('resta/', views.restar, name='resta'),

    # ex: http://localhost:8000/app/resta/19/10/
    path('resta/<int:primer>/<int:segundo>/', views.Rresta, name='Rrest'),

    # ex: http://localhost:8000/app/multiplica/
    path('multiplica/', views.multiplicar, name='multiplica'),

    # ex: http://localhost:8000/app/multiplica/6/7/
    path('multiplica/<int:primer>/<int:segundo>/', views.Rmultiplica, name='Rmult'),
]
