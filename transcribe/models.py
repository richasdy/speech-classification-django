from django.db import models
from django.utils import timezone
from audio.models import File

# Create your models here.

class Transcribe(models.Model):
    File = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    # applicant_id = models.IntegerField(default=0) # in byte
    raw = models.TextField(default="")
    verbatim_text = models.TextField(default="")
    action_text = models.TextField(default="")
    enthusiasm_text = models.TextField(default="")
    focus_text = models.TextField(default="")
    imagine_text = models.TextField(default="")
    integrity_text = models.TextField(default="")
    smart_text = models.TextField(default="")
    solid_text = models.TextField(default="")
    speed_text = models.TextField(default="")
    totality_text = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.File
