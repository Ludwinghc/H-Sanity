# Generated by Django 4.2.2 on 2023-10-17 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0006_rename_hotel_establishment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Establishment',
            new_name='EstablishmentModel',
        ),
    ]
