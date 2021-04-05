import RPi.GPIO as GPIO
from time import sleep
import httplib2
import json
import urllib.request
import os
import jwt
import pyrebase

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


 config = {

  "apiKey": "JQTcsq6HNfJlZyx30iPJOCOw93YHI1AE8QRyBnBv",

  "authDomain": "arduinofirebaseconnectio-d58e9.firebaseapp.com",

  "databaseURL": "https://arduinofirebaseconnectio-d58e9-default-rtdb .firebaseio.com",

  "storageBucket": "arduinofirebaseconnectio-d58e9.appspot.com",

 # "serviceAccount": "path/to/serviceAccountCredentials.json"

}
firebase = pyrebase.initialize_app(config)

GPIO.setup(4,GPIO.IN)


def update_firebase():

	moisture= GPIO.input(4)
	if moisture is not None:
		
		firebase.post(moisture)			
			
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)

	
	

	while True:
		update_firebase()
		sleep(5)

