# Generated by Django 4.2.2 on 2023-10-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditory', '0006_remove_audit_establishment_delete_establishmentaudit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
