from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

import logging

from core.models import Wihda, Exercise, Summary_wihda, School, Modakira, Tadaroj, Year
from core.google_drive import display_files

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'core/home.html')


def school_year(request, year):
    school = School.objects.get(school_year=year)
    return render(request, 'core/school_year.html', {'school': school})


def exercise_wihda(request):
    wihda = request.GET.get('wihda', None)
    school_year_id = request.GET.get('school_year_id', None)
    wihda = get_object_or_404(Wihda, name=wihda, school_id=school_year_id)
    exercises = Exercise.objects.filter(wihda=wihda).order_by('order_name')
    context = {
        'wihda': wihda,
        'exercises': exercises
    }
    return render(request, 'core/exercises_wihda.html', context)


def exercise(request, pk):
    exc = get_object_or_404(Exercise, id=pk)
    wihda = exc.wihda
    id_exercise = exc.link.split('/')[5]

    context = {
        'exc': exc,
        'wihda': wihda,
        'id_exercise': id_exercise,
    }
    if exc.solution_link:
        id_exc_solution = exc.solution_link.split('/')[5]
        context['id_exc_solution'] = id_exc_solution
    return render(request, 'core/exercise.html', context)


def summary_wihda(request, id_wihda):
    wihda = get_object_or_404(Wihda, id=id_wihda)
    summaries = Summary_wihda.objects.filter(
        wihda=wihda).order_by('order_name')
    context = {'summaries': summaries, 'wihda': wihda}
    return render(request, 'core/summary_wihda.html', context)


def summary(request, pk):
    summ = get_object_or_404(Summary_wihda, id=pk)
    wihda = summ.wihda
    id_summary = summ.link.split('/')[5]

    context = {
        'summ': summ,
        'wihda': wihda,
        'id_summary': id_summary
    }

    return render(request, 'core/summary.html', context)


def modakirat_wihda(request):
    wihda = request.GET.get('wihda', None)
    school_year_id = request.GET.get('school_year_id', None)
    wihda = get_object_or_404(Wihda, name=wihda, school_id=school_year_id)
    modakirat = Modakira.objects.filter(wihda=wihda).order_by('order_name')
    context = {
        'wihda': wihda,
        'modakirat': modakirat
    }
    return render(request, 'core/modakirat_wihda.html', context)


def modakira(request, pk):
    modakira = get_object_or_404(Modakira, id=pk)
    wihda = modakira.wihda
    id_modakira = modakira.link.split('/')[5]

    context = {
        'modakira': modakira,
        'wihda': wihda,
        'id_modakira': id_modakira,
    }
    return render(request, 'core/modakira.html', context)


def year(request):
    years = Year.objects.all()
    return render(request, 'core/years.html', {'years': years})


def tadarojat_year(request, id_year):
    year = get_object_or_404(Year, id=id_year)
    tadarojat = Tadaroj.objects.filter(
        year=year).order_by('order_name')
    context = {'tadarojat': tadarojat, 'year': year}
    return render(request, 'core/tadarojat_year.html', context)


# def tadaroj(request, pk):
#     tadaroj = get_object_or_404(Tadaroj, id=pk)
#     year = tadaroj.year
#     id_tadaroj = tadaroj.link.split('/')[5]

#     context = {
#         'tadaroj': tadaroj,
#         'year': year,
#         'id_tadaroj': id_tadaroj
#     }

#     return render(request, 'core/tadaroj.html', context)


@staff_member_required
def tool(request):
    logger.info('Begin execution view tool')
    context = {}
    drive_id = request.GET.get('drive_id', None)
    drive_name = request.GET.get('drive_name', None)
    connect_all_files = request.GET.get('connect_all_files', None)

    logger.info(f'drive_id = {drive_id}')
    logger.info(f'drive_name = {drive_name}')
    logger.info(f'connect_all_files = {connect_all_files}')

    if connect_all_files is not None:
        logger.info('variable connect_all_files is not None')
        files = display_files(query=drive_id)
        for file in files:
            link = f"https://drive.google.com/file/d/{file['id']}/view?usp=sharing"
            exercise = Exercise.objects.filter(link=link)
            if not exercise.exists():
                wihda = Wihda.objects.get(name=drive_name)
                link = f"https://drive.google.com/file/d/{file['id']}/view?usp=sharing"
                exercise = Exercise.objects.create(
                    name=file['name'], link=link, wihda=wihda)
                exercise.save()
        context['connect_all_files'] = None

    if drive_id is not None:
        files = display_files(query=drive_id)
        returned_files = []
        for file in files:
            link = f"https://drive.google.com/file/d/{file['id']}/view?usp=sharing"
            exercise = Exercise.objects.filter(link=link)
            if not exercise.exists():
                returned_files.append(file)
        display_connect = True
    else:
        returned_files = display_files()
        display_connect = False

    context = {'returned_files': returned_files,
               'display_connect': display_connect}
    if drive_name:
        context['drive_name'] = drive_name
    if drive_id:
        context['drive_id'] = drive_id

    return render(request, 'core/tool.html', context)
