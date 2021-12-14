from flask import Flask
import RPi.GPIO as GPIO
import time

channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

app = Flask(__name__)

@app.route("/on")
def on(): 
  while True:
     state = GPIO.input(channel)

     print(f"Etat de la diode: {state}")

     if state == 0:
       GPIO.output(channel, GPIO.HIGH)
     else:
       GPIO.output(channel, GPIO.LOW)

     time.sleep(1)

  return "<p>Hello, World!</p>"

@app.route("/off")
def off():
    GPIO.output(channel, GPIO.LOW)
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
