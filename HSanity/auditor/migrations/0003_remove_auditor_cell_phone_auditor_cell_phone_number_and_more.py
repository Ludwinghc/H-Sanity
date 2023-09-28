# Generated by Django 4.2.5 on 2023-09-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditor', '0002_alter_auditor_no_id_alter_auditor_cell_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditor',
            name='cell_phone',
        ),
        migrations.AddField(
            model_name='auditor',
            name='cell_phone_number',
            field=models.BigIntegerField(null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='auditor',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='auditor',
            name='mail',
            field=models.EmailField(max_length=50, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='auditor',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='auditor',
            name='passkey',
            field=models.CharField(max_length=10, null=True, verbose_name='Clave'),
        ),
    ]
