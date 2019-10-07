from django.db import models
from django.utils import timezone
from audio.models import File

# Create your models here.
class Grade(models.Model):
    File = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    # applicant_id = models.IntegerField(default=0) # in byte
    action_grade = models.TextField(default="")
    enthusiasm_grade = models.TextField(default="")
    focus_grade = models.TextField(default="")
    imagine_grade = models.TextField(default="")
    integrity_grade = models.TextField(default="")
    smart_grade = models.TextField(default="")
    solid_grade = models.TextField(default="")
    speed_grade = models.TextField(default="")
    totality_grade = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)