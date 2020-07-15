from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

import logging

from core.models import Wihda, Exercise, Summary_wihda
from core.google_drive import display_files

logger = logging.getLogger(__name__)


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


def summary_wihda(request, id_wihda):
    wihda = get_object_or_404(Wihda, id=id_wihda)
    summaries = Summary_wihda.objects.filter(wihda=wihda)
    context = {'summaries': summaries, 'wihda': wihda}
    return render(request, 'core/summary_wihda.html', context)


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
