from django.db import models
from django.utils import timezone
from audio.models import File

# Create your models here.
class Grade(models.Model):
    File = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    # applicant_id = models.IntegerField(default=0) # in byte
    action_grade = models.IntegerField(default=0)
    enthusiasm_grade = models.IntegerField(default=0)
    focus_grade = models.IntegerField(default=0)
    imagine_grade = models.IntegerField(default=0)
    integrity_grade = models.IntegerField(default=0)
    smart_grade = models.IntegerField(default=0)
    solid_grade = models.IntegerField(default=0)
    speed_grade = models.IntegerField(default=0)
    totality_grade = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.File

    def get_action():
        return 0