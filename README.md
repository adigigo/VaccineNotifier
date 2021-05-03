# VaccineNotifier
A Python script to get data from the Aarogya Sethu API to find vaccine appointments for 7 days past a specific date in a specific pincode

The program uses the official CoWIN API which is publically available here : https://apisetu.gov.in/public/api/cowin#/

Before you Begin:
1) I have tried to use as many in-built libraries as possible. You would need to install the 'requests' library if you do not have it installed. 
  
  You can install Requests by using 
   here : 
  pip install requests
  
  or 
  
  conda install requests
  
 2) For the telegram and email notification, you would need to set up a Telegram Bot account and enable App Passwords in Gmail

Follow this link : https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637554658548216477-2576856839&rd=1 for generating app specific passwords and use your email ID and the generated password in the script (DO NOT FOR THE LOVE OF GOD SHARE THE APP PASSWORD TO ANYONE!)

Follow this link : https://www.codementor.io/@garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay to create and connect a Telegram Bot to the script. 

3) Run the python script by navigating to the folder in the terminal (you can google how to  do this) and runnign the command 
  python3 FILENAME.py
  
  where FILENAME is the name of the python file
  
  Hope this helps! Stay Safe everyone!

Telegram Screenshot
![WhatsApp Image 2021-05-03 at 3 54 48 PM](https://user-images.githubusercontent.com/43105718/116865929-2e46e700-ac28-11eb-9895-80482b2924b3.jpeg)


Email Screenshot
![Capture](https://user-images.githubusercontent.com/43105718/116865968-3e5ec680-ac28-11eb-98dd-2ea6d1bdf984.PNG)

