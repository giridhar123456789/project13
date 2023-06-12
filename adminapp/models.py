from django.db import models

# Create your models here.
class Jobs(models.Model):
    jobid=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    skills=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)