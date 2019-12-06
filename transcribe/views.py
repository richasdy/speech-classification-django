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

from google.cloud import speech
from google.cloud import storage
import os


# bucket_name = 'kemitraan-telkom-1550985641715.appspot.com' #pak ikhsan
bucket_name = 'quantum-engine-248003.appspot.com' #pak ikhsan
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sspk-owner.json" #pak ikhsan
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/My_First_Project-2c46ff0c115f.json" #pak ikhsan


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
    file.save()

    transcribe = get_object_or_404(Transcribe, File_id=request.POST['id'])
    # transcribe.action_text = request.POST['action_text']
    # transcribe.enthusiasm_text = request.POST['enthusiasm_text']
    # transcribe.focus_text = request.POST['focus_text']
    # transcribe.imagine_text = request.POST['imagine_text']
    # transcribe.integrity_text = request.POST['integrity_text']
    # transcribe.smart_text = request.POST['smart_text']
    # transcribe.solid_text = request.POST['solid_text']
    # transcribe.speed_text = request.POST['speed_text']
    # transcribe.totality_text = request.POST['totality_text']
    transcribe.verbatim_text = request.POST['verbatim_text']
    transcribe.updated_at = timezone.now()
    transcribe.save()

    return HttpResponseRedirect(reverse('transcribe:edit', args=(file.id,)))


def save(request):
    return redirect('/transcribe/')

def delete(request, id):
    return HttpResponse("You're voting on audio delete %s." % id)

def process(request, id):

    file = get_object_or_404(File, id=id)
    TranscribeThread.run(file)
    return HttpResponseRedirect(reverse('transcribe:edit', args=(id,)))

import threading
class TranscribeThread(threading.Thread):
    def run(file):
        try:
            hasil_transcribe = transcriptingstreo('gs://'+bucket_name+'/'+file.name)
        except:
            hasil_transcribe = transcriptingmono('gs://'+bucket_name+'/'+file.name)

        try:
            transcribe = Transcribe.objects.get(File_id=file.id)
        except Transcribe.DoesNotExist:
            transcribe = Transcribe.objects.create(File_id=file.id)

        transcribe.raw = hasil_transcribe
        transcribe.verbatim_text = hasil_transcribe
        transcribe.save()

def transcriptingstreo(filename):
    ##global hasiltranscript
    hasiltranscript=''
    #client=speech.SpeechClient()
    #audio=speech.types.RecognitionAudio(uri=filename)
    #config=speech.types.RecognitionConfig(
    #    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,language_code='id-ID',audio_channel_count=2,
    #enable_separate_recognition_per_channel=True
    #)
    operation=speech.SpeechClient().long_running_recognize(
        config=speech.types.RecognitionConfig(encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='id-ID',audio_channel_count=2,enable_separate_recognition_per_channel=True)
        ,audio=speech.types.RecognitionAudio(uri=filename))
    print('Waiting for transcriptingstreo to complete...')
    #response = operation.result(timeout=10000)
    for result in operation.result(timeout=10000).results:
           hasiltranscript += str(result.alternatives[0].transcript)
    return hasiltranscript

def transcriptingmono(filename):
    #global hasiltranscript
    #client = speech.SpeechClient()
    #audio = speech.types.RecognitionAudio(uri=filename)
    #config = speech.types.RecognitionConfig(
    #    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16, language_code='id-ID'
    #)
    #operation = client.long_running_recognize(config=config, audio=audio)
    hasiltranscript = ''
    operation = speech.SpeechClient().long_running_recognize(
        config=speech.types.RecognitionConfig(encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
                                              language_code='id-ID')
        , audio=speech.types.RecognitionAudio(uri=filename))
    print('Waiting for transcriptingmono to complete...')
    response = operation.result(timeout=10000)
    for result in response.results:
        hasiltranscript += str(result.alternatives[0].transcript)

    return hasiltranscript