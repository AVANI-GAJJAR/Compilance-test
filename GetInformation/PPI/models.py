from django.db import models

# Create your models here.
class IngestData(models.Model):
    file= models.FileField(upload_to = 'filename')
