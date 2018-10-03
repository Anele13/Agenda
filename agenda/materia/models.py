from django.db import models

# Create your models here.
class Evento(models.Model):
    id = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    persona = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    aula = models.CharField(max_length=50)
