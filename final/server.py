from flask import Flask
from flask import send_file
import RPi.GPIO as GPIO
import cv2

import features.distance as distance
import features.ia as ia
import features.led as led
import features.person_detector as person_detector 

last_person_filename = "/home/pi/data/person.jpeg"
last_picture_filename = "/home/pi/data/test_annotated.jpeg"


GPIO.setmode(GPIO.BCM)



print("**************** Configuration *************")
print(f"** LED Anode : GPIO_{led.gpio_led}")
print(f"** Détecteur distance ECHO: GPIO_{distance.gpio_echo}")
print(f"** Détecteur distance TRI : GPIO_{distance.gpio_tri}")
print(f"** Fichier dernière image prise: {last_picture_filename}")
print(f"** Fichier dernière personne prise: {last_person_filename}")
print("********************************************")


app = Flask(__name__)

@app.route("/on")
def on():
  led.start_blink()
  return "<p>Hello, World!</p>"

@app.route("/off")
def off():
  led.stop_blink()
  return "<p>Hello, World!</p>"

@app.route("/shoot")
def shoot():
  cap = cv2.VideoCapture(0)
  cap.set(3,640)
  cap.set(4,480)

  success, img = cap.read()
  result, objectInfo = ia.getObjects(img,0.50,0.2)
  print(objectInfo)
  cv2.imwrite(last_picture_filename, result)

  if "person" in str(objectInfo):
    print("une personne a été trouvée")
    cv2.imwrite(last_person_filename, result)

  return send_file(last_picture_filename, mimetype='image/jpg')

@app.route("/last-person")
def last_person():
  return send_file(last_person_filename, mimetype='image/jpg')


@app.route("/")
def web():
  _distance = distance.get_distance()
  return f"""
<html>
  <head>
    <style>
.row {{
  display: flex;
}}

.column {{
  flex: 33.33%;
  padding: 5px;
}}
    </style>
  </head>
  <body>
    <h1>Qastia Detector</h1>
    <p>
      <form>
        <input Type="button" value="Reshooter" onClick="history.go(0)">
      </form>
    </p>
    <p>Distance: {_distance}</p>
    <div class="row">
      <div class="column">
        <img src="/shoot">
      </div>
       <div class="column">
        <img src="/last-person">
      </div>
    </div>
  </body>
</html>
  """

@app.route("/distance")
def distance_action():
  _distance = distance.get_distance()
  return f"<p>distance {distance}</p>"

@app.route("/persons")
def web_persons():
  return person_detector.generate_html()

@app.route("/download/<filename>")
def persons_web(filename):
  return send_file(person_detector.DATA_DIR + "/" + filename, mimetype='image/jpg')



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
