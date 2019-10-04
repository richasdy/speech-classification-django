from django.contrib import admin

# Register your models here.

from .models import Applicant
from .models import File

admin.site.register(Applicant)
admin.site.register(File)