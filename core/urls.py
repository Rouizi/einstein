from django.urls import path
from core import views

urlpatterns = [
    path('1as', views.first_year, name='first_year'),
    path('2as', views.second_year, name='second_year'),
    path('3as', views.third_year, name='third_year'),
    path('exercise-wihda', views.exercise_wihda, name='exercise_wihda'),
    path('tool', views.tool, name='tool'),
]
