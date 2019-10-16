from django.shortcuts import render

from django.http import HttpResponse
from grade.models import Grade
from audio.models import File
from transcribe.models import Transcribe

def index(request):
    # return HttpResponse("Hello, world. You're at the dashboard index.")
    target_count = 100

    file_count = File.objects.count()
    file_percent = file_count/target_count*100

    transcribe_count = Transcribe.objects.count()
    transcribe_percent = transcribe_count/target_count*100

    grade_count = Grade.objects.count()
    grade_percent = grade_count/target_count*100

    grade_list = Grade.objects.order_by('-total')[:5]
    context = {
        'grade_list':grade_list,

        'file_count':file_count,
        'file_percent':file_percent,

        'transcribe_count':transcribe_count,
        'transcribe_percent':transcribe_percent,
        
        'grade_count':grade_count,
        'grade_percent':grade_percent,
        }
    return render(request, 'dashboard/index.html', context)