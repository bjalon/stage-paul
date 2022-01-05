

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

channel = 4
GPIO.setup(channel, GPIO.OUT)

state = GPIO.input(channel)  
print(f"Etat de la diode: {state}")
if state == 0:
  GPIO.output(4, GPIO.HIGH)
else:
  GPIO.output(4, GPIO.LOW)
