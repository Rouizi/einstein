from django.urls import path
from core import views

urlpatterns = [
    path('1as', views.premiere_annee, name='premiere_annee'),
    path('2as', views.deuxieme_annee, name='deuxieme_annee'),
    path('3as', views.troisieme_annee, name='troisieme_annee'),
]