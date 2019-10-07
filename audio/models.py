from django.db import models
from django.utils import timezone

class Applicant(models.Model):
    name = models.CharField(max_length=100,default="")
    note = models.TextField(default="")

    def __str__(self):
        return self.name

class File(models.Model):
    # Applicant = models.ForeignKey(Applicant, on_delete=models.SET_NULL, null=True)
    applicant_id = models.IntegerField(default=0) # in byte
    name = models.CharField(max_length=100,default="")
    note = models.TextField(default="")
    location = models.TextField(default="")
    location_cloud = models.TextField(default="")
    size = models.IntegerField(default=0) # in byte
    duration = models.IntegerField(default=0) #in minute
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def speech2text():
        return "hello transcriber output"