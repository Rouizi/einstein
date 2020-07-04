from django.shortcuts import render, get_object_or_404
from core.models import Wihda

def index(request):
    return render(request, 'core/home.html')

def premiere_annee(request):
    wihdat_first_year = Wihda.objects.filter(school__school_year='الأولى ثانوي')
    return render(request, 'core/first_year.html', {'wihdat_first_year': wihdat_first_year})

def deuxieme_annee(request):
    wihdat_second_year = Wihda.objects.filter(school__school_year='الثانية ثانوي')
    print(wihdat_second_year)
    return render(request, 'core/second_year.html', {'wihdat_second_year': wihdat_second_year})

def troisieme_annee(request):
    wihdat_third_year = Wihda.objects.filter(school__school_year='الثالثة ثانوي')
    return render(request, 'core/third_year.html', {'wihdat_third_year': wihdat_third_year})

def exercise_wihda(request):
    wihda = request.GET.get('wihda', None)
    wihda = get_object_or_404(Wihda, name=wihda)

