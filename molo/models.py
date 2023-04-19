from django.db import models
import datetime

# Create your models here.

class Molo(models.Model):
    molo_name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.molo_name