from django.shortcuts import render, get_object_or_404

from core.models import Wihda, Exercise


def index(request):
    return render(request, 'core/home.html')


def first_year(request):
    wihdat_first_year = Wihda.objects.filter(
        school__school_year='الأولى ثانوي')
    return render(request, 'core/first_year.html', {'wihdat_first_year': wihdat_first_year})


def second_year(request):
    wihdat_second_year = Wihda.objects.filter(
        school__school_year='الثانية ثانوي')
    print(wihdat_second_year)
    return render(request, 'core/second_year.html', {'wihdat_second_year': wihdat_second_year})


def third_year(request):
    wihdat_third_year = Wihda.objects.filter(
        school__school_year='الثالثة ثانوي')
    return render(request, 'core/third_year.html', {'wihdat_third_year': wihdat_third_year})


def exercise_wihda(request):
    wihda = request.GET.get('wihda', None)
    school_year_id = request.GET.get('school_year_id', None)
    wihda = get_object_or_404(Wihda, name=wihda, school_id=school_year_id)
    exercises = Exercise.objects.filter(wihda=wihda)
    context = {
        'wihda': wihda,
        'exercises': exercises
    }
    return render(request, 'core/exercises_wihda.html', context)
