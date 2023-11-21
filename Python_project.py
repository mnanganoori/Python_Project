import pyautogui
import time
import subprocess
import os
import pywhatkit as pwkit
import yagmail
import geocoder
import requests
import wikipedia

print("|---------------------------------------------------------------------------------------|")
print("|\t\t\t\tWelcome to my Python Project\t\t\t\t|")
print("|---------------------------------------------------------------------------------------|")

#Notepad Automation 
def openNotepad():
    print("Opening Notepad.....")
    subprocess.Popen(["notepad.exe"])
    time.sleep(3)
    
def closeNotepad():
    print("Notepad closed...")
    # subprocess.run(["taskkill", "/f", "/im", "notepad.exe"])
    pyautogui.hotkey("alt", "f4")
    time.sleep(3)
    pyautogui.typewrite('n', interval=0.1)

#Sending whatsapp messages instantly
def send_whatsappMessage():
    print("Send a whatsapp message")
    phn_number :str
    phn_number = input("Enter phone number: ")
    what_message :str
    what_message = input("Enter your message: ")
    pwkit.sendwhatmsg_instantly(phn_number,what_message+"(Automated)", tab_close=True)


#Sending Emails 
def send_Email():
    emai_address  = 'kumarmaheshn2021@gmail.com'
    emai_password = 'gpbeaaxzllbfvfbb'
    yag = yagmail.SMTP(emai_address, emai_password)
    to_address:str
    to_address = input("Enter the TO address: ")
    subject:str
    subject = input("Enter your mail SUBJECT: ")
    contents:str
    contents  = input("Enter the mail contents: ")
    yag.send(to=to_address, subject= subject, contents= contents)
    yag.close()

#Get your location (Longitude and Latitude)
def getLocation():
    location = geocoder.ip('me')
    latitude, longitude = location.latlng
    try:
        print(f"\tCurrent latitude is: {latitude}, Current Longitude is: {longitude}")
    except Exception as e:
        print(f"Error locating: {e}")

#Get your wikipedia information
def get_wiki_info():
    topic = input("Enter the topic name: ")
    try:
        summary = wikipedia.summary(topic, sentences = 3)
        # summary = wikipedia.summary(topic, sentences = 1)
        print(summary)
    except wikipedia.exceptions.PageError as e:
        print("Exception while searching for the topic"+ e)


#Get your current location 
def getLocation_City():
    location = geocoder.ip('me')
    latitude, longitude = location.latlng
    url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}'
    response = requests.get(url)
    location_data = response.json()
    #print(location_data)
    city = location_data.get('address', {}).get('city', '')
    if not city:
        city = location_data.get('address', {}).get('town', '')
    if not city:
        city = location_data.get('address', {}).get('village', '')
    HNO = location_data.get('address', {}).get('house_number', '')
    state = location_data.get('address', {}).get('state', '')
    country = location_data.get('address', {}).get('country', '')
    county = location_data.get('address', {}).get('county', '')
    postal_code = location_data.get('address', {}).get('postcode', '')
    print(f"\tHNO:{HNO}, {city}, {county}, {state}, {country}, {postal_code}")

while True:
    print("""   
        1: Notepad Automation
        2: Open Chrome
        3: Send WhatsApp Message
        4: Send Email
        5. Display Geolocation  
        6: Current Address
        7: Wikipedia Information
          """)
    print("Choose 0 to exit")
    ch = input("Enter your choice: ")
    # print(ch)

    match int(ch):
        case 0:
            print("Exiting....")
            break
        case 1:
            openNotepad()
            pyautogui.write("Success")
            closeNotepad()
        case 2:
            os.system("chrome") 
            print("|---------------------------------------------------------|")
            print("\tOpened Chrome")
            print("|---------------------------------------------------------|")
        case 3:
            print("|---------------------------------------------------------|")
            send_whatsappMessage()
            print("|---------------------------------------------------------|")
            print("\tWhatsapp Message sent successfully")
            print("|---------------------------------------------------------|")
        case 4:
            print("|---------------------------------------------------------|")
            send_Email()
            print("|---------------------------------------------------------|")
            print("\tEmail sent successfully") 
            print("|---------------------------------------------------------|")
        case 5:
            print("|---------------------------------------------------------|")
            print("\tCollecting information")
            getLocation()
            print("|---------------------------------------------------------|")
            print("\tLocation fetched successfully....")
            print("|---------------------------------------------------------|")
        case 6:
           print("|--------------------------------------------------------------------------|")
           getLocation_City()
           print("|--------------------------------------------------------------------------|")
        case 7: 
            print("|---------------------------------------------------------|")
            print("\tWikipedia...")
            get_wiki_info()
            print("|---------------------------------------------------------|")
        case _:
            print("|---------------------------------------------------------|")
            print("\tChoose a valid option")
            print("|---------------------------------------------------------|")
    if(int(ch) == 0):
        break