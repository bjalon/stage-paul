from flask import Flask
from flask import send_file
import RPi.GPIO as GPIO
import threading
import time
from picamera import PiCamera
from time import sleep

is_blink_requested = False
camera = PiCamera()

def diode_loop():
  while True:
    if is_blink_requested:
      state = GPIO.input(channel)
      print(f"Etat de la diode: {state}")

      if state == 0:
        GPIO.output(channel, GPIO.HIGH)
      else:
        GPIO.output(channel, GPIO.LOW)
    time.sleep(1)

threading.Thread(target=diode_loop).start()


channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

app = Flask(__name__)

@app.route("/on")
def on():
  global is_blink_requested
  is_blink_requested = True
  return "<p>Hello, World!</p>"

@app.route("/off")
def off():
  global is_blink_requested
  is_blink_requested = False
  return "<p>Hello, World!</p>"

@app.route("/shoot")
def shoot():
  filename = '/tmp/test.jpg'
  camera.start_preview()
  camera.capture(filename)
  camera.stop_preview()
  return send_file(filename, mimetype='image/jpg')
