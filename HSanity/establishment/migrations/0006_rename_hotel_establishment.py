# Generated by Django 4.2.2 on 2023-10-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0005_rename_establishment_hotel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotel',
            new_name='Establishment',
        ),
    ]