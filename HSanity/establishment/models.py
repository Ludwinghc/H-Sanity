from django.db import models

# Create your models here.

class Establishment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length=100, null=True)
    photo = models.ImageField(verbose_name='Foto del Establecimiento', upload_to='images/hotelProfile', null=True)
    address = models.CharField(verbose_name='Direccion', max_length=50, null=True)
    contact = models.BigIntegerField(verbose_name='Contacto', null=True)
    mail = models.CharField(verbose_name='Correo', max_length=50, null=True)
    website = models.CharField(verbose_name='Pagina Web', max_length=100, null=True)
    rut = models.BigIntegerField(verbose_name='RUT', null=True)

    def __str__(self):
        row = str(self.id) + "-" + self.name
        return row
    
    def delete(self, using=None, keep_perents=False):
        self.photo.storage.delete(self.photo.name)
        super().delete()