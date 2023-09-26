# Generated by Django 4.2.2 on 2023-09-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0002_establishment_address_establishment_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establishment',
            name='image',
        ),
        migrations.AddField(
            model_name='establishment',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/hotelProfile', verbose_name='Foto del establecimiento'),
        ),
    ]