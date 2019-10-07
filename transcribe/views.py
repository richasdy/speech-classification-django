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
from .models import Transcribe
from django.utils import timezone



def index(request):
    file_list = File.objects.all()
    context = {'file_list': file_list}
    return render(request, 'transcribe/index.html', context)


def edit(request, id):
    file = get_object_or_404(File, id=id)
    
    try:
        transcribe = Transcribe.objects.get(File_id=id)
    except Transcribe.DoesNotExist:
        transcribe = Transcribe.objects.create(File_id=file.id)

    context = {'file': file, 'transcribe': transcribe}
    return render(request, 'transcribe/edit.html', context)
    

def update(request, id):
    file = get_object_or_404(File, id=request.POST['id'])
    file.note = request.POST['note']
    file.save()

    transcribe = get_object_or_404(Transcribe, File_id=request.POST['id'])
    transcribe.action_text = request.POST['action_text']
    transcribe.enthusiasm_text = request.POST['enthusiasm_text']
    transcribe.focus_text = request.POST['focus_text']
    transcribe.imagine_text = request.POST['imagine_text']
    transcribe.integrity_text = request.POST['integrity_text']
    transcribe.smart_text = request.POST['smart_text']
    transcribe.solid_text = request.POST['solid_text']
    transcribe.speed_text = request.POST['speed_text']
    transcribe.totality_text = request.POST['totality_text']
    transcribe.updated_at = timezone.now()
    transcribe.save()

    return HttpResponseRedirect(reverse('transcribe:edit', args=(file.id,)))

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