<h1 align="center">
     Technical Challenge for
Practical Test at DSI :woman_technologist:
</h1>
DSI technical challenge.  Process automation, optical character processing (OCR) and API development using Python, pyautogui, pytesseract, and FastAPI.

##  :beginner: About
This project is a proposed solution to the technical challenge proposed by the company Design Systems Inno (DSI), which seeks to develop an integrated system that automates the extraction of textual information of documents on a local computer and execute actions based on that information through an API.

##  :paperclip: Implementation
For this project, a simulated form has been implemented in the medical records of a medical clinic. The Django framework has been used to develop a template for this form, taking advantage of visual tools such as Bootstrap. Additionally, a model called "Patient" has been configured to store each added item in the Django database PostgreSQL. 

The information to complete the form is obtained from a file called "patients.txt", which contains the information to fill the fields. However, the "Birthplace" and "Blood Type" fields are not present in this file. To obtain this data, the program reads images using the Pytesseract library. Then, using PyAutoGUI commands, the requested fields are completed, carrying out several processes to analyze this information. By using FastApi endpoints, it is possible to perform mouse movements and extract text from images with POST requests.

Below, the operation of the project is detailed more precisely.
## Demo

https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/0b7fbd16-44c0-45fc-99e1-6e10b8f6236f

### Full Demo

See Full Demo [here](https://youtu.be/aE_iiBIizqs).
###  :file_folder: File Structure
The structure and directories of the project are presented in this section:

```
.
└───DSI-Automation-Challenge-LinaBallesteros-
│    └───medical_form
│        ├───medical_form
│        │   ├─── settings.py
│        │   ├─── urls.py            
│        │   └───__pycache__
│        ├───medical_records
│        │   ├───media
│        │   ├───migrations     
│        │   │   └───__pycache__
│        │   ├───static
│        │   │   └───imgs       
│        │   ├───templates
│        │   │
│        │   ├─── api_automation.py  
│        │   ├─── rpa_functions.py
│        │   ├─── views.py
│        │   ├─── urls.py       
│        │   └───__pycache__
│        ├─── db.sqlite3
│        ├─── manage.py
│        └───__pycache__
│
├─── requirements.txt
└─── README.md

```

## :zap: Installation
Follow these instructions to run the program in your machine.

1. Clone the project on your machine.
    ```bash
      git clone https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-.git
    ```
2.  Activate your virtual environment if you are using one. If you're not using a virtual environment, you can skip this step.

    ```bash
      venv\Scripts\activate   
    ```
3. Go to the project directory.

    ```bash
      cd .\DSI-Automation-Challenge-LinaBallesteros-\
    ```
4. Install the dependencies/libraries required using `pip`

    ```bash
      pip install -r requirements.txt
    ```
5. Install the [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract). For Windows users, it is essential to install the Tesseract OCR, you can install it [here](https://github.com/UB-Mannheim/tesseract/wiki) and find more information about this library in the official [docs](https://pypi.org/project/pytesseract/).
6. After installing the Tesseract OCR, you need to manually change the path of your tesseract.exe file by going to the [api_automation.py]() file that includes the path to the executable file, as shown here:
    ```bash
      pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```
## :package: Commands
Once you have completed the installation steps, you are ready to set up the servers that will host both the Django form and the FastAPI api.

1. Go to the following project directory. Make sure you are in the correct folder.

    ```bash
      cd .\DSI-Automation-Challenge-LinaBallesteros-\medical_form\
    ```
2. To migrate the Django application's data model to the configured database, run the following command from the specified path.
  
  ```bash
    python manage.py migrate
  ```
3. Create a superuser to access the database with:

 ```bash
    python manage.py createsuperuser
  ```
   
4. To start the Django development server, run the following command in your terminal from the specified path. Please start the server with the indicated parameters and on the specified port to avoid problems with the execution of the program. 

 ```bash
   python manage.py runserver 0.0.0.0:5000
 ```

5. Check that the server is running at [http://localhost:5000](http://localhost:5000). In order for the program's features to be compatible to the greatest extent possible, the suggested browser is Microsoft Edge. Once you entered, you should see the following:

![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/05bb29c7-18db-490b-b7ee-3d1c647993af)

6. Open a new terminal (without ending the one you started before for the Django server) and go to the following project directory. Make sure you are in the correct folder. 

 ```bash
   cd .\DSI-Automation-Challenge-LinaBallesteros-\medical_form\medical_records\
 ```
7. To start the FastAPI server, run the following command in your terminal from the specified path. Please start the server with the indicated parameters and on the specified port to avoid problems with the execution of the program.

```bash
   uvicorn api_automation:app --reload
 ```
8. To check that the server is running, you can go to [http://localhost:8000/](http://localhost:8000/). You should see the following:

![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/c816c37b-92b0-47f4-8d15-6ee9d3095633)

9. After doing all of these steps, you are ready to run the program. Make sure both servers are always running at the same time and on the specified ports.

##  :wrench: Usage

### :notebook: Note
It is important to highlight that the use of the PyAutoGUI library can be complex on machines other than the one on which the project was developed, since the behavior of the mouse and keyboard may vary depending on the operating system, the machine's configuration and other factors. You may need to adjust the waiting times, or some parameters so that the program works correctly in different environments. Despite what was said above, the program was designed in such a way that its implementation should be carried out in the best possible way on other Windows operating system machines. Even so, key configurations and keyboard shortcuts may vary depending on the nature of each system, as well as delay times for pages to load. For example, for pressing "tab" key on my personal machine this occurs with just pressing a key and is not the result of a configuration of keys, as might be the case on some other Windows machine, so in the project this is reflected in the keys pressed specified for the program or when switching between programs with the "alt" and "tab" keys, as well as other configurations determined in the project. Please keep the above in mind in case you receive inconsistencies when running the program.

1. To start the automation, go to [http://localhost:5000](http://localhost:5000), where the form is located.
   
![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/05bb29c7-18db-490b-b7ee-3d1c647993af)

:warning: **Warning:** Once the automation starts, do not move the mouse or use your computer keyboard. If you want to stop the process at any point, you just have to bring your mouse to the upper left corner of the screen, which will activate pyautogui's fail safe that stops any process that is being carried out. It is recommended to [review this functionality](https://youtu.be/eAIJ-hYzYeo?si=O6wUIf45tx9UuoL4) in case you have never worked with PyAutoGUI.

2. Click the 'Autofill' button located in the top right corner of the screen. Once you have clicked it, the automation will start.
   
![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/ecccb0d3-2405-4027-840b-6af0e6ce46d0)

3. That's it, once the process is complete, and if everything went well, you should see the records added to the database in Django Admin.

![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/2185e3f3-0023-4fbe-8fb3-ab179bbfc52a)


## :nut_and_bolt: Implementation Details

As mentioned before, this project has a base made with the Django framework to facilitate the view of the form. To do this, an application called 'medical_records' was created, which stores the files necessary to execute the form template, such as the views.py file and the urls.py file. The urls.py file specifies the routes that allow you to start the automation and register the data of each patient in the model.

The data that is read is taken from a file called 'patients.txt' that looks like this:

```bash
   Name;Id Number;Date of Birth;Birthplace;Gender;Occupation;Marital Status;Phone Number;Emergency Contact;Allergies;Blood Type;Past Surgeries
  "Maria Fernandez;1452485698;20/03/1990; ;Female;Lawyer;Single;3123456789;3134567890;None; ;None"
 ```

This file contains different categories of information separated each by semicolons. However, in the 'Birthplace' and 'Blood Type' categories, there is no data and they are specified with blank spaces, this is because the program will search for this information according to 2 specific images, which are found stored in a [Google Drive folder](https://drive.google.com/drive/folders/1CUNegFUhnkfiiUsYTnPOVgIwWfiEdT8w?usp=sharing).

In the first execution of the program, both images are displayed by opening the browser, so that the user can view the information or image from which the program is extracting the text and converting it into what will later be analyzed in 2 ways, that is:

The image 'ss_birthplaces.png' is analyzed to recover the place of birth of the person and after recovering that data, the department that city corresponds to is searched by reading a csv called 'Departamentos_y_municipios_de_Colombia_20240428 (1).csv' downloaded from the [official open data page](https://www.datos.gov.co/Mapas-Nacionales/Departamentos-y-municipios-de-Colombia/xdk5-pm3f/data_preview) of the government of Colombia. This is so that the program establishes a single input format in the form field as follows: "CITY, DEPARTMENT", avoiding the problem of creating ambiguities that may exist when a person, for example, fills out the formula.


![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/d2d73dbf-615c-4a62-80bf-87f956675283)


The image 'ss_blood_types.png' is analyzed to retrieve the person's blood type. It does this by rectifying a regular expression using the re library, defined for blood types, example: 'O+', 'AB-', etc. An important clarification is that the key configuration with pyautogui when entering data enters the '+' sign as '*'. Once each blood type corresponds to which patient is identified, it is assigned according to the current patient being registered.


![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/894fb11d-91d5-4ce6-8d70-104b3e49dd0f)


**Mouse movements:** Some movements that the mouse makes during execution may seem strange, but they have a justification:

1. **_'Default' or start movement when registering a patient:_** This is done for the purpose of being able to click in the upper left part and for the 'tabs' to be coordinated so that the first 'tab' corresponds to the 'button' Autofill' and the second 'tab' so that it already places the program in the first field to fill out.

2.**_Central movement, or that moves to the center of the screen:_** It is done with the purpose of preventing the cursor from being located on top of any title, button or tool where text may appear on top of it when placing the mouse on it, this was done in It began when a screenshot was taken and the text was extracted from the image. However, this functionality does not seem viable to be carried out on any computer due to the differences in the resolution of the screens, the zoom that the user has defined, the quality with which the image can appear when taking the screenshot, among other factors that could affect the text extraction sensitivity of pytesseract, since it is a library that is not completely accurate when extracting the text and that in this project is used by extracting text from an image that is in the directory of files.

**Default Browser:** In order to maximize the compatibility of the program components, a Microsoft Edge tab opens by default to display photos in Google Drive.
Again, the clarification is made that loading times may vary depending on the machine on which it is executed and the quality of its connection.

**Using API Endpoints in FastAPI:** You can check the deployed endpoints by going to [http://localhost:8000/docs](http://localhost:8000/docs), and you can also test these directly from this site. The root endpoint is a message only to refer the user to the api documentation, if needed. The mouse movement endpoint was explained above. It is necessary to clarify that to use the text to image conversion endpoint, the logic within this endpoint was made taking into account the images that were going to be treated, so, if you want to test this endpoint from docs, you can download the images from Google Drive and upload them directly. Posts requests are made through the 'requests' library.


![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/346d4118-2e86-4902-a560-2c2f1ae959f6)

![image](https://github.com/linasofi13/DSI-Automation-Challenge-LinaBallesteros-/assets/140737132/e863b6c1-94f3-45ff-8e2b-6d2f4aa0e366)



## :star2: Credits & Author
- All credits in the creation of the challenge correspond to Design Systems Inno (DSI)
- [Lina Ballesteros](https://github.com/linasofi13) is the author of the developed solution.
  
##  :lock: License
Licence
