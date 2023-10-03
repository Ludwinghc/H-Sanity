from django.db import models

# Create your models here.

class Auditor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre", null=True)
    last_name = models.CharField(max_length=100, verbose_name="Apellido", null=True)
    no_id = models.BigIntegerField(verbose_name="Numero de Identificación", null=True)
    mail = models.EmailField(verbose_name="Correo", max_length=50, null=True)
    passkey = models.CharField(max_length=10, verbose_name="Clave", null=True)
    cell_phone_number = models.BigIntegerField(verbose_name="Celular", null=True)

    def __str__(self):
        row = str(self.id) + "-" + self.name
        return row
