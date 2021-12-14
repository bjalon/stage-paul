from flask import Flask
import RPi.GPIO as GPIO
import threading
import time

is_blink_requested = False

def diode_loop():
  while True:
    print("Bloucle")
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

@app.route("/hello")
def hello_world():
  return "<p>Hello, World!</p>"
