# Generated by Django 4.2.2 on 2023-11-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0008_rename_establishmentmodel_establishment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='photo',
            field=models.ImageField(null=True, upload_to='media\\images\\hotelProfile', verbose_name='Foto del Establecimiento'),
        ),
    ]