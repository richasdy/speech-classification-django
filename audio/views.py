from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.conf import settings
import asyncio



from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from werkzeug.utils import secure_filename
from pydub import AudioSegment
import os
from google.cloud import storage

from .models import File

bucket_name = 'quantum-engine-248003.appspot.com' #pak ikhsan
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/My_First_Project-2c46ff0c115f.json" #pak ikhsan

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

def save_local(request):

    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']

        file = File.objects.create()
        file.name = myfile.name
        file.location = settings.MEDIA_URL
        file.size = myfile.size
        file.save()

        # upload = UploadLocalThread()
        # upload.run(myfile)
        # UploadLocalThread.run(myfile)
        asyncio.run(UploadLocalThread.run(myfile))

    return redirect('/audio/')

import threading
# from django.core.files import UploadedFile
class UploadLocalThread(threading.Thread):
    async def run(file):
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

def save(request):

    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']

        file = File.objects.create()
        file.name = myfile.name.split('.')[0] + ".wav"
        file.location = settings.MEDIA_URL
        file.size = myfile.size
        file.save()

        UploadCloudThread.run(myfile, file.id)

    return redirect('/audio/')

class UploadCloudThread(threading.Thread):
    def run(file, id):

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        #jika ekstensi bukan wav, ubah jadi wav dulu
        if filename.split('.')[1] != 'wav':
            dst = filename.split('.')[0] + ".wav"
            sound = AudioSegment.from_file(os.path.join(settings.MEDIA_ROOT, filename))
            sound.export(os.path.join(settings.MEDIA_ROOT, dst), format='wav')
            os.remove(os.path.join(settings.MEDIA_ROOT, filename))
            filename = dst
        
        sound = AudioSegment.from_wav(os.path.join(settings.MEDIA_ROOT, filename))
        sound = sound.set_channels(1)
        sound = sound.set_sample_width(2)
        sound.export(os.path.join(settings.MEDIA_ROOT, filename), format='wav')

        #upload ke bucket_name yang sudah di tentukan diawal kode
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_filename(os.path.join(settings.MEDIA_ROOT, filename))
        blob.make_public()
        location_cloud = blob._get_download_url()

        os.remove(os.path.join(settings.MEDIA_ROOT, filename))

        file = get_object_or_404(File, id=id)
        file.location_cloud = location_cloud
        file.save()

def delete(request, id):
    file = get_object_or_404(File, id=id)
    filename = file.name
    file.delete()

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.delete()

    return redirect('/audio/')

def process(request, id):
    return HttpResponse("You're voting on audio process %s." % id)

#mengembalikan tipe file
# def file_allowed(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions