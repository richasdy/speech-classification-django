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


def index(request):
    file_list = File.objects.all()
    context = {'file_list': file_list}
    return render(request, 'grade/index.html', context)


def edit(request, id):
    file = get_object_or_404(File, id=id)
    context = {'file': file}
    return render(request, 'grade/edit.html', context)
    

def update(request, id):
    file = get_object_or_404(File, id=request.POST['id'])
    file.note = request.POST['note']
    file.save()

    return HttpResponseRedirect(reverse('grade:edit', args=(file.id,)))

def process(request, id):
    return HttpResponse("You're voting on grade process %s." % id)