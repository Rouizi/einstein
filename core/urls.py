from django.urls import path
from core import views

urlpatterns = [
    path('school-year/<year>/', views.school_year, name='school_year'),
    path('exercise-wihda/', views.exercise_wihda, name='exercise_wihda'),
    path('exercise/<int:pk>/', views.exercise, name='exercise'),
    path('summary_wihda/<id_wihda>/', views.summary_wihda, name='summary_wihda'),
    path('summary/<int:pk>/', views.summary, name='summary'),
    path('tool', views.tool, name='tool'),
]
