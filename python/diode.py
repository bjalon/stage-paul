

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

channel = 4
state = GPIO.input(channel)  
print(f"Etat de la diode: {state}")
if state == 0:
  GPIO.output(4, GPIO.HIGH)
else:
  GPIO.output(4, GPIO.LOW)
