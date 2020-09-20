from django.urls import path
from core import views

urlpatterns = [
    path('school-year/<year>', views.school_year, name='school_year'),
    path('exercise-wihda', views.exercise_wihda, name='exercise_wihda'),
    path('summary_wihda/<id_wihda>', views.summary_wihda, name='summary_wihda'),
    path('tool', views.tool, name='tool'),
]
