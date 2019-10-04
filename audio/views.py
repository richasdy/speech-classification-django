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

from .models import File

def index(request):
    file_list = File.objects.all()
    # output = file_list
    # return HttpResponse(output)

    # template = loader.get_template('audio/index.tut.html')
    # context = {
    #     'file_list': file_list,
    # }
    # return HttpResponse(template.render(context, request))

    context = {'file_list': file_list}
    # return render(request, 'audio/index.tut.html', context)

    # context = {'audio_list': File.objects.all()}
    return render(request, 'audio/index.html', context)

class IndexView(generic.ListView):
    template_name = 'audio/index.tut.html'
    context_object_name = 'file_list'

    def get_queryset(self):
        return File.objects.all()

def edit(request, id):
    # return HttpResponse("You're looking at audio edit %s." % id)

    # try:
    #     file = File.objects.get(id=id)
    #     context = {'file': file}
    # except File.DoesNotExist:
    #     raise Http404("File does not exist")

    file = get_object_or_404(File, id=id)
    context = {'file': file}
    
    # return render(request, 'audio/detail.tut.html', context)
    return render(request, 'audio/edit.html', context)
    

def update(request, id):
    # response = "You're looking at the results of audio update %s."
    # return HttpResponse(response % id)

    file = get_object_or_404(File, id=request.POST['id'])
    # file.name = request.POST['name']
    file.note = request.POST['note']
    # file.location = request.POST['location']
    file.save()

    return HttpResponseRedirect(reverse('audio:edit', args=(file.id,)))

uploaded_file_list = [];

def save(request):
    # response = "You're looking at the results of audio save %s. "+request.FILES['file']
    # return HttpResponse(response % id)

    uploaded_file_list.clear()

    # if request.method == 'POST':
    #     uploaded_file = request.FILES['file']
    #     uploaded_file_list.append(uploaded_file)
    #     fs = FileSystemStorage()
    #     audio_name = fs.save(uploaded_file.name, uploaded_file)
    #     audio_url = fs.url(audio_name)
    #     audio_byte_size = fs.size(audio_name)/1000000
    #     # audio_megabyte_size = "%.2f" % audio_byte_size
    #     audio_megabyte_size = "%.2f" % audio_byte_size
    #     # audio_size = str(audio_megabyte_size)+ " mb"
    #     audio_size = audio_megabyte_size

    #     file = File(title=audio_name, aplicants_name="Admin (Hard Coded)", directory=audio_url, size=audio_size)
    #     file.save()

    #     print(audio_url)

    return redirect('/audio/')

    # data3 = File.objects.all()
    # return render(request, 'django_app/audio-upload.html', {"data3" : data3})


def delete(request, id):
    return HttpResponse("You're voting on audio delete %s." % id)

def process(request, id):
    return HttpResponse("You're voting on audio process %s." % id)
