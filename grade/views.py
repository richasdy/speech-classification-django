from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from audio.models import File
from .models import Grade
from transcribe.models import Transcribe
from django.utils import timezone
from grade import annaction
from grade import annenthusiasm
from grade import annfocus
from grade import annimagine
from grade import annintegrity
from grade import annsmart
from grade import annsolid
from grade import annspeed
from grade import anntotality


def index(request):
    file_list = File.objects.all()
    context = {'file_list': file_list}
    return render(request, 'grade/index.html', context)


def edit(request, id):
    
    file = get_object_or_404(File, id=id)
    
    try:
        grade = Grade.objects.get(File_id=id)
    except Grade.DoesNotExist:
        grade = Grade.objects.create(File_id=file.id)

    context = {'file': file, 'grade': grade}
    return render(request, 'grade/edit.html', context)
    

def update(request, id):

    file = get_object_or_404(File, id=request.POST['id'])
    file.note = request.POST['note']
    file.save()

    grade = get_object_or_404(Grade, File_id=request.POST['id'])
    grade.action_grade = request.POST['action_grade']
    grade.enthusiasm_grade = request.POST['enthusiasm_grade']
    grade.focus_grade = request.POST['focus_grade']
    grade.imagine_grade = request.POST['imagine_grade']
    grade.integrity_grade = request.POST['integrity_grade']
    grade.smart_grade = request.POST['smart_grade']
    grade.solid_grade = request.POST['solid_grade']
    grade.speed_grade = request.POST['speed_grade']
    grade.totality_grade = request.POST['totality_grade']
    grade.total = (int(grade.action_grade) + int(grade.enthusiasm_grade) + int(grade.focus_grade) + int(grade.imagine_grade) + int(grade.integrity_grade) + int(grade.smart_grade) + int(grade.solid_grade) + int(grade.speed_grade) + int(grade.totality_grade))/9
    grade.updated_at = timezone.now()
    grade.save()
    
    return HttpResponseRedirect(reverse('grade:edit', args=(file.id,)))

def process(request, id):

    try:
        transcribe = Transcribe.objects.get(File_id=id)
    except Transcribe.DoesNotExist:
        transcribe = Transcribe.objects.create(File_id=id)
    
    try:
        grade = Grade.objects.get(File_id=id)
    except Grade.DoesNotExist:
        grade = Grade.objects.create(File_id=id)

    grade.action_grade = annaction.run(transcribe.verbatim_text)
    grade.enthusiasm_grade = annenthusiasm.run(transcribe.verbatim_text)
    grade.focus_grade = annfocus.run(transcribe.verbatim_text)
    grade.imagine_grade = annimagine.run(transcribe.verbatim_text)
    grade.integrity_grade = annintegrity.run(transcribe.verbatim_text)
    grade.smart_grade = annsmart.run(transcribe.verbatim_text)
    grade.solid_grade = annsolid.run(transcribe.verbatim_text)
    grade.speed_grade = annspeed.run(transcribe.verbatim_text)
    grade.totality_grade = anntotality.run(transcribe.verbatim_text)

    grade.total = (int(grade.action_grade) + int(grade.enthusiasm_grade) + int(grade.focus_grade) + int(grade.imagine_grade) + int(grade.integrity_grade) + int(grade.smart_grade) + int(grade.solid_grade) + int(grade.speed_grade) + int(grade.totality_grade))/9
    grade.updated_at = timezone.now()
    grade.save()

    return HttpResponseRedirect(reverse('grade:edit', args=(id,)))