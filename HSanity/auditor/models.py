from django.db import models
# from django.core.exceptions import ValidationError


# Create your models here.
class Auditor(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, verbose_name='name', null=True)
  last_name = models.CharField(max_length=100, verbose_name='last name', null=True)
  No_Id = models.IntegerField(verbose_name='No° Id', null=True)
  mail = models.EmailField(verbose_name='mail', max_length=50, null=True)
  passkey = models.CharField(max_length=10, verbose_name='passkey', null=True)
  cell_phone = models.IntegerField(verbose_name='phone', null=True)
  
  def __str__(self):
    row = str(self.id) + "-" + self.name
    return row
