# Generated by Django 4.2.1 on 2024-04-28 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0007_remove_patient_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='photo',
        ),
    ]