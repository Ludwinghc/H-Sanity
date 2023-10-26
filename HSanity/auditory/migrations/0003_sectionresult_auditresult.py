# Generated by Django 4.2.2 on 2023-10-24 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auditory', '0002_rename_rating_audit_scoretopass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditory.section')),
            ],
        ),
        migrations.CreateModel(
            name='AuditResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auditory.audit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]