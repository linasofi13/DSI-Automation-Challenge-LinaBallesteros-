from django.contrib import admin
from django.urls import path, include
from medical_records import views as medical_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medical_records.urls')),

]
