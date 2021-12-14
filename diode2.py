import time
import RPi.GPIO as GPIO

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

while 1==1:
  state = GPIO.input(channel)

  #print(f"Etat de la diode: {state}")

  if state == 0:
    GPIO.output(channel, GPIO.HIGH)
  else:
    GPIO.output(channel, GPIO.LOW)

  time.sleep(1)

