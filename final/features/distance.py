import RPi.GPIO as GPIO
import time

gpio_echo = 20
gpio_tri = 21

GPIO.setmode(GPIO.BCM)

def get_distance():
  GPIO.setup(gpio_tri,GPIO.OUT)
  GPIO.setup(gpio_echo,GPIO.IN)

  GPIO.output(gpio_tri, False)
  time.sleep(0.1)
  GPIO.output(gpio_tri, True)
  time.sleep(0.00001)
  GPIO.output(gpio_tri, False)

  while GPIO.input(gpio_echo)==0:  ## Emission de l'ultrason
    debutImpulsion = time.time()

  while GPIO.input(gpio_echo)==1:   ## Retour de l'Echo
    finImpulsion = time.time()

  distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

  print(f"La distance est de : {str(distance)}cm")
  return distance
