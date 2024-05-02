# Generated by Django 4.2.1 on 2024-04-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('insurance_information', models.TextField(blank=True, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('past_surgeries', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
