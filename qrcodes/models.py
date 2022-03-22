from distutils.command.upload import upload
from django.db import models

class Flange(models.Model):
    flange_number = models.IntegerField()
    torque = models.IntegerField()
    aks_number = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.flange_number)