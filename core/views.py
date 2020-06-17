from django.shortcuts import render

def index(request):
    return render(request, 'core/home.html')

def premiere_annee(request):
    return render(request, 'core/premiere_annee.html')

def deuxieme_annee(request):
    return render(request, 'core/deuxieme_annee.html')

def troisieme_annee(request):
    return render(request, 'core/troisieme_annee.html')

