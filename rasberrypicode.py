import RPi.GPIO as GPIO
from time import sleep
import httplib2
import json
import os
import jwt
import 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

firebase = firebase.FirebaseApplication('https://arduinofirebaseconnectio-d58e9-default-rtdb.firebaseio.com/', None)
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

