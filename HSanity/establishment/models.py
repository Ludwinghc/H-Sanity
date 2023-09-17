from django.db import models

# Create your models here.

class Establishment():
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=100),
    image = models.ImageField(null=True, upload_to=-'/images'),
    address = models.CharField(max_length=50),
    contact = models.BigIntegerField(),
    mail = models.CharField(max_length=50),
    website = models.CharField(max_length=100),
    rut = models.BigIntegerField(),