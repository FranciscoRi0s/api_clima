
from django.db import models

class Informacion(models.Model):
    id=models.IntegerField(primary_key=True)
    temperatura = models.CharField(max_length=255) 
    humedad = models.CharField(max_length=255)  
    latitud = models.CharField(max_length=255)  
    longitud = models.CharField(max_length=255)  

    class Meta:
        managed = True
        db_table = 'informacion'
