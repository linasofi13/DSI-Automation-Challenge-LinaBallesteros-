from django.contrib import admin
from django.urls import path, include
from .views import medical_form_view, add_patient_data_view, auto_fill_data_view
from .models import Patient

urlpatterns = [
    path('admin/', admin.site.urls), # access to database
    path('', medical_form_view, name='medical_form_view'), # default view is the medical form
    path('patient_data/', add_patient_data_view, name='add_patient_data_view'), # add to model
    path('auto_fill/', auto_fill_data_view, name='auto_fill_data_view') # start automation 
]
