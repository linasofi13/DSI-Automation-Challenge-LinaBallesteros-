from django.shortcuts import render, redirect
from .models import Patient
import time, datetime, csv, pyautogui, pyperclip
from .rpa_functions import *
from fastapi import FastAPI
from django.http import HttpResponse



def medical_form_view(request):
    return render(request, 'medical_record_form.html')

def add_patient_data_view(request):
    if request.method == 'POST':
        #try:
            name = request.POST.get('patient_name')
            id_number = request.POST.get('id_number')
            date_of_birth = request.POST.get('date_of_birth')
            birthplace = request.POST.get('birthplace')
            gender = request.POST.get('gender')
            occupation = request.POST.get('occupation')
            marital_status = request.POST.get('marital_status')
            phone_number = request.POST.get('phone_number')
            emergency_contact = request.POST.get('emergency_contact')
            allergies = request.POST.get('allergies')
            blood_type = request.POST.get('blood_type')
            past_surgeries = request.POST.get('past_surgeries')
            
            # save patient
            patient = Patient(
                name=name,
                id_number=id_number,
                date_of_birth=date_of_birth,
                birthplace=birthplace,
                gender=gender,
                occupation=occupation,
                marital_status=marital_status,
                phone_number=phone_number,
                emergency_contact=emergency_contact,
                allergies=allergies,
                blood_type=blood_type,
                past_surgeries=past_surgeries
            )
            patient.save()
            print("patient added")
            
            return redirect('medical_form_view')
        
        #except Exception as data_error:
        #    error_message = "An error occurred while saving patient data. Check that the fields are correct."
         #   return render(request, 'medical_record_form.html', {'error_message': error_message})
    else:
        print("patient not added")
        return render(request, 'medical_record_form.html')

def auto_fill_data_view(request): # triggered after clicking the autofill button
    try:
        start_autofill() # function stored in rpa_functions file
        return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 16px; 
                    color: #333; 
                }
                h2 {
                    font-weight: bold; 
                }
                strong {
                    font-weight: bold; 
                }
            </style>
        </head>
        <body>
            <h2>The automation process was completed successfully.</h2><br><br>
            
            <p>The process has terminated correctly.</p><br>
            
        </body>
        </html>
    """)
    except Exception: # pyautogui exception of stop automation
        return HttpResponse("""
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                font-size: 16px; 
                color: #333; 
            }
            h2 {
                font-weight: bold; 
            }
            strong {
                font-weight: bold; 
            }
        </style>
    </head>
    <body>
        <h2>The automation process was stopped. This could be due to several reasons:</h2><br><br>
        
        <ol>
            <li>Ensure that you are running both servers: Django on localhost:5000 and FastAPI on localhost:8000.</li>
            <li><strong>You may have inadvertently halted the program by activating PyAutoGUI's fail-safe function.</strong></li>
            <li>There might be an internal problem with the server.</li>
            <li>There is a possibility of compatibility issues with the operating system or some features provided by PyAutoGUI.</li>
        </ol><br>
        
        <p>To resolve this issue, please follow these steps:</p><br>
        <ol>
            <li>Refresh the localhost page or restart the servers.</li>
            <li>Make sure you are in the correct directory where your servers are located.</li>
        </ol><br>
        
        <p>If the issue persists, please check your server logs for more detailed error messages or contact the project administrator for further assistance. Check the GitHub repository for this project for more detailed information.</p>
    </body>
    </html>
    """)
