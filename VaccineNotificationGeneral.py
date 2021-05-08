# COVID-19 Vaccination Appointment Tracker (03/05/2021)
# A Python script that tracks vaccination appoints for the next 7 days for a specific pincode using the CoWin API
# Most of the libraries are inbuilt but the user needs to install the 'requests' library

# with <3 by Adarsh Parameswaran, Kozhikode,Kerala

import requests
import json
import smtplib
from datetime import date,datetime
import time
import sys

# Function to send an email with the appointment details 'appt' as input. 

def send_mail(appt):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('your_email_id','your_app_password')   # Get 2FA and a app-specific password for Gmail
    
    subject = 'Vaccine Appointment available near you!'
    body = "Hey! I found some vaccine appointments near you!\n"+appt
    
    msg = f"Subject : {subject} \n\n {body}"
    
    server.sendmail('senders_email','receivers_email',msg)
    
    print(" Hey! E-Mail has been sent!")
    server.quit()
    
## Specify Pincode before running
pincode = '392110'

def AppointmentCheck():

    today = date.today()
    current_date = today.strftime("%d-%m-%Y")   ##Gets todays Date

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  ##Gets Current time of checking

    ## CoWIN API
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={current_date}"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0'}

    response = requests.get(url,headers = headers)

    if response.status_code != 200:
        print ("Error!")
        exit()
    else:
        data = response.json()
        centers = data['centers']   #Gets all the vaccination centers and their corresponding details
        
        if len(centers) == 0:
            print(f"No Appointments found in the next 7 days from {current_date} : Last Check at {current_time}")
        
        else:
            res = {}
            for center in centers:
                a = center['name'] + f" ({center['fee_type']})"
                b = []
                for session in center['sessions']:
                    b.append(str(f"{session['date']} // Age Limit :{session['min_age_limit']} // Capacity : {session['available_capacity']}"))
                    res[a] = b
            
            a = ''
            for center,data in res.items():
                a += ("\n"+center+"\n\n")
                for dates in data:
                    a += str(dates+"\n")

            #Sends the appointment details via telegram
            requests.get(f"https://api.telegram.org/YOUR_TELEGRAM_BOT_ID/sendMessage?chat_id=YOUR_CHAT_ID&text={a}")
            
            #Sends email with the details
            #send_mail(a)
            
            print("Found Vaccination Dates! Exiting..")
            exit()


print("COVID-19 Vaccination Appointment Checker\n")

while(True):
    AppointmentCheck()
    time.sleep(60*30)