import time, datetime, csv, pyautogui, webbrowser, pytesseract, re, os, requests
from PIL import Image
import requests 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

patients_list = [] # list of patients, each patient is a dictionary
category_list = [] # headers

api_url = 'http://127.0.0.1:8000'

timeout_seconds = 5

current_dir = os.path.dirname(__file__)

colombia_places_dataset = "Departamentos_y_municipios_de_Colombia_20240428 (1).csv"


def open_file(patients_list):
    file_path = os.path.join(current_dir, 'patients.txt')
    with open(file_path, 'r') as file:
        categories_line = next(file)
        categories = categories_line.strip().split(';') # first line contains categories or headers of each column

        for line in file:
            patient_dict = {} # a dictionary to have {category: value} for each patient
            patient = line.strip().replace('"', '').split(';')
            
            for category, data in zip(categories, patient):
                patient_dict[category] = data  
            patients_list.append(patient_dict)
            
        
def move_default_position():    
    pyautogui.moveTo(1, 1) # go to the top left corner
    pyautogui.moveRel(140, 200, duration=1) # move diagonally
    pyautogui.click()
    pyautogui.press("tab") # first tab is autofill button
    pyautogui.press("tab") # second tab starts going through the fields, starting by name

def move_center_position():
    screen_width, screen_height = pyautogui.size()  
    
    half_screen_width = screen_width // 2
    half_screen_height = screen_height // 2 # center mouse pointer to avoid unexpected text to appear by placing it in an specific place
    
    pyautogui.moveTo(half_screen_width, half_screen_height, 1)

def open_edge_web_address(web_address):
    pyautogui.press("win") # pressing windows key to open edge
    time.sleep(2)
    pyautogui.write("Microsoft Edge") 
    time.sleep(1)
    pyautogui.press("enter") 
    time.sleep(3) # a few seconds for it to load
    pyautogui.write(web_address) 
    time.sleep(3)
    pyautogui.press("enter") 
    time.sleep(3)

# a function to find the department of a given city to set the same format to a field, reading a csv    
def find_department(birthplace, colombia_places_dataset):
    file_path = os.path.join(current_dir, colombia_places_dataset)
    with open(file_path, newline='', encoding='utf-8') as file:
        read_csv = csv.DictReader(file) 
        for row in read_csv:
            if row['MUNICIPIO'].upper() == birthplace.upper():
                return row['DEPARTAMENTO'].upper()
    return None



def set_special_fields(current_patient, patients_list, category):
        
    if current_patient['Name'] == patients_list[0]['Name']: # if it is the first element open the browser and screenshot

        move_center_position()

        if category == "Birthplace":
            web_address = "https://drive.google.com/file/d/1ty4dNvAQR2rbwVw_L_W0PGW6J4Wtolm-/view?usp=sharing"
        
        else:
            web_address = "https://drive.google.com/file/d/14InQg447_ePIMpTTebPaJd9x__eE-IjG/view?usp=sharing"
        
        open_edge_web_address(web_address)
        
        # time.sleep(5) # loading time
        screenshot = pyautogui.screenshot() 
        screenshot.save("patients_birthplaces.png")
        
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)
        
    if category == "Birthplace":
        image_path = os.path.join(current_dir, "ss_birthplaces.png")
    else:
        image_path = os.path.join(current_dir, "ss_blood_types.png")

    with open(image_path, "rb") as file:
        file_image = {"image": file}
        try: 
            path_segment = '/text_to_image/'
            request_url = api_url+path_segment
            response = requests.post(request_url, files=file_image, timeout=timeout_seconds)
        
            if response.status_code == 200:# if succesful
                print('The POST request was succesful')
                response_data = response.json() 
                data_dict = response_data['result']
                result = data_dict[current_patient['Name']]
                print(result)
                if category == 'Birthplace':
                    # try: # if the given city exists
                        department = find_department(result, colombia_places_dataset)
                        print(department)
                        birthplace_completed = result.upper() + ', ' + department
                        print(birthplace_completed)
                        return birthplace_completed
                    #except Exception as e:
                        #return "Birthplace not Found"
                else:
                    return result
            else:
                print('Error in the POST request:', response.status_code)
                print('Error message: ', response.text)
        except requests.Timeout:
            print('The request has exceeded the maximum timeout of', timeout_seconds, 'seconds. The request has been rejected.')


def start_autofill():
    open_file(patients_list)
    # print(patients_list)
    for patient_dict in patients_list:   
        path_segment = '/move_default_position/'
        request_url = api_url+path_segment
        try:
            response = requests.post(request_url, timeout=timeout_seconds) 
            
        except requests.Timeout:
            print('The request has exceeded the maximum timeout of', timeout_seconds, 'seconds. The request has been rejected.')
        pyautogui.scroll(300) 
        for category, value in patient_dict.items():
            if category == "Past Surgeries":
                # time.sleep(1)   
                pyautogui.typewrite(value, interval=0.1)
                # time.sleep(1)
                pyautogui.press("tab")  
                pyautogui.press("enter") # submit button
                
                break
            # time.sleep(1)
            if category == 'Gender':
                pyautogui.press("enter")
                if value == "Male":
                    pyautogui.press('down')
                    pyautogui.press("enter")
                    # pyautogui.press("tab")
                elif value == "Female":
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press("enter")    
                    #pyautogui.press("tab")
                elif value == "Other":
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press("enter")
                    # pyautogui.press("tab")
                
            if category == 'Birthplace':
                birthplace_to_write = set_special_fields(patient_dict, patients_list, category)
                print(birthplace_to_write)
                pyautogui.write(birthplace_to_write)
                # time.sleep(1)
                # pyautogui.press("tab")
                
            if category == 'Marital Status':
                if value == "Single":
                    pyautogui.press('right')
                    pyautogui.press('right')
                    pyautogui.press('right')
                    pyautogui.press('right')
                    # pyautogui.press("enter")
                    # pyautogui.press("tab")
                    
                elif value == "Married":
                    
                    pyautogui.press('right')
                    # pyautogui.press("enter")
                    # pyautogui.press("tab")
                    
                elif value == "Divorced":
                    
                    pyautogui.press('right')        
                    pyautogui.press('right')
                    # pyautogui.press("enter")
                    # pyautogui.press("tab")
                    # 
                elif value == "Widowed":
                    
                    pyautogui.press('right')
                    pyautogui.press('right')
                    pyautogui.press('right')
                    # pyautogui.press("enter")
                    # pyautogui.press("tab")
                    # 
                # time.sleep(1)
            if category == "Blood Type":
                blood_type_to_write = set_special_fields(patient_dict, patients_list, category)
                print(blood_type_to_write)
                pyautogui.write(blood_type_to_write)
                time.sleep(1)
                pyautogui.press("tab")
                
            else: 
                # time.sleep(1)   
                pyautogui.typewrite(value, interval=0.1)
                # time.sleep(1)
                pyautogui.press("tab")
