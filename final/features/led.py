import RPi.GPIO as GPIO
import threading
from time import sleep


gpio_led = 4
is_blink_requested = False

def diode_loop():
  while True:
    if is_blink_requested:
      state = GPIO.input(gpio_led)
      print(f"Etat de la diode: {state}")

      if state == 0:
        GPIO.output(gpio_led, GPIO.HIGH)
      else:
        GPIO.output(gpio_led, GPIO.LOW)
    sleep(1)

threading.Thread(target=diode_loop).start()

GPIO.setup(gpio_led, GPIO.OUT)

def start_blink():
  global is_blink_requested
  is_blink_requested = True

def stop_blink():
  global is_blink_requested
  is_blink_requested = False
