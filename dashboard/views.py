from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the dashboard index.")

    context = {}
    return render(request, 'dashboard/index.html', context)