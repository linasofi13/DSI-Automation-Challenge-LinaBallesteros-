from fastapi import FastAPI, UploadFile, File
from django.core.wsgi import get_wsgi_application
import os
from PIL import Image
from fastapi.responses import JSONResponse
from rpa_functions import *
import pytesseract
import requests

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI()

@app.get("/")
async def root(): # this is only to refer the user to the api documentation, if needed
    return {"message": "Welcome to my API. Please refer to the documentation for usage instructions."}

@app.post("/move_default_position/")
async def move_default_position():
    try:
        pyautogui.moveTo(1, 1) # go to the top left corner
        pyautogui.moveRel(140, 200, duration=1) # move diagonally
        pyautogui.click()
        pyautogui.press("tab") # first tab is autofill button
        pyautogui.press("tab") # second tab starts going through the fields, starting by name
        
        return {"message": "Mouse moved successfully"}
    except Exception as error:
        print("Error:", error)
        return {"error": str(error)}

@app.post("/text_to_image/")
async def text_to_image(image: UploadFile = File(...)): # takes an image as argument
    try:
        with Image.open(image.file) as image_birthplaces: 
            text_from_image = pytesseract.image_to_string(image_birthplaces) # using pytesseract library
            print(text_from_image)

        names_categories_list = [] # to clean list elements
        
        pattern_name_blood_type = r"([A-Z][a-z]+\s[A-Z][a-z]+\s[ABO]{1,2}[+-])" # a regex that matches names and a blood type after, ex: 'Pepito Perez O+'
        pattern_matches = re.findall(pattern_name_blood_type, text_from_image)
        text_from_image = text_from_image.split("\n")
            
        for element in text_from_image:
            if element != 'Patient Birthplace' and element != '' and element != "Patient Blood Type": # clean the given text
                names_categories_list.append(element)

        patients_categories_dict = {}

        for element in names_categories_list:
            string_divided = element.split()
            name = ' '.join(string_divided[:2])
            if pattern_matches:
                result = string_divided[-1]
            else:
                result = ' '.join(string_divided[2:])
            patients_categories_dict[name] = result
                
        # print(patients_categories_dict)
        
        return {"result": patients_categories_dict}
      
    except Exception as e:
        # print(e)
        return {"error": str(e)}
