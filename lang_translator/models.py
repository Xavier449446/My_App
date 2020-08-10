from django.db import models

class Audio(models.Model):
    audio = models.FileField(upload_to='media/')