from django.urls import path
from core import views

urlpatterns = [
    path('school-year/<year>/', views.school_year, name='school_year'),
    path('exercise-wihda/', views.exercise_wihda, name='exercise_wihda'),
    path('exercise/<int:pk>/', views.exercise, name='exercise'),
    path('summary_wihda/<id_wihda>/', views.summary_wihda, name='summary_wihda'),
    path('summary/<int:pk>/', views.summary, name='summary'),
    path('modakirat_wihda/', views.modakirat_wihda, name='modakirat_wihda'),
    path('modakira/<int:pk>/', views.modakira, name='modakira'),
    path('year/', views.year, name='year'),
    path('tadarojat_year/<int:id_year>/',
         views.tadarojat_year, name='tadarojat_year'),
    # path('tadaroj/<int:pk>/', views.tadaroj, name='tadaroj'),
    path('ads/', views.ads, name='ads'),
    path('tool', views.tool, name='tool'),
]
