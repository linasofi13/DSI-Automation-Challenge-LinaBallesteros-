from django.db import models
from datetime import date

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default='')
    id_number = models.CharField(max_length=20, blank=True, null=True, default='')
    date_of_birth = models.DateField(default=date(2000, 1, 1))  
    birthplace = models.CharField(max_length=100, blank=True, null=True, default='')
    gender = models.CharField(max_length=10, blank=True, null=True, default='')
    occupation = models.CharField(max_length=100, blank=True, null=True, default='')
    marital_status = models.CharField(max_length=35, blank=True, null=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, null=True, default='')
    emergency_contact = models.CharField(max_length=100, blank=True, null=True, default='')
    blood_type = models.CharField(max_length=5, blank=True, null=True, default='')
    allergies = models.TextField(blank=True, null=True, default='')
    past_surgeries = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return self.name if self.name else 'Patient'
