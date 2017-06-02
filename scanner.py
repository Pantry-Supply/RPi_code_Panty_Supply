
import requests
import json
import jsonify
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

button1=11
button2=13

led1=18
led2=16
ledGO=15

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(11, GPIO.OUT, initial=0)
GPIO.setup(13, GPIO.OUT, initial=0)
GPIO.setup(37, GPIO.OUT, initial=0)

GPIO.setup(led1, GPIO.OUT, initial=0)
GPIO.setup(led2, GPIO.OUT, initial=0)
GPIO.setup(ledGO, GPIO.OUT, initial=0)


while(1):
        GPIO.output(ledGO, 1)
	if GPIO.input(button1)==1:
                GPIO.output(ledGO, 0)
                one = -1
		print("Button 1 was pressed")
		while(one < 0):
                        one=raw_input()
                print(one)
                dataToSend = {"barcode":one}
		addItem = requests.post('https://pantrysupply.herokuapp.com/insert', data=dataToSend)
                print(addItem.text)
                ##print(source.json()["result"]["item_name"])
		GPIO.output(led1, 1)
                sleep(.2)
		GPIO.output(led1, 0)
		GPIO.output(ledGO, 1)
		one = -1

	if GPIO.input(button2)==1:
                two=-1
                GPIO.output(ledGO, 0)
		print("Button 2 was pressed")
		while(two<0):
                        two=raw_input()
                print(two)
                deleteItem = requests.get('https://pantrysupply.herokuapp.com/bcadjustdown/%s' % two)
		print(deleteItem.text)
		GPIO.output(led2, 1)
                sleep(.2)
		GPIO.output(led2, 0)
		GPIO.output(ledGO, 1)
		two = -1
