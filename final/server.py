from flask import Flask
from flask import send_file
import RPi.GPIO as GPIO
import features.distance as distance
import features.ia as ia
import features.led as led

GPIO.setmode(GPIO.BCM)



print("**************** Configuration *************")
print(f"** LED Anode : GPIO_{led.gpio_led}")
print(f"** Détecteur distance ECHO: GPIO_{distance.gpio_echo}")
print(f"** Détecteur distance TRI : GPIO_{distance.gpio_tri}")
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
  filename = "/home/pi/data/test_annotated.jpeg"

  success, img = cap.read()
  result, objectInfo = ia.getObjects(img,0.50,0.2)
  print(objectInfo)
  cv2.imwrite(filename, result)
  return send_file(filename, mimetype='image/jpg')


@app.route("/")
def web():
  return f"""
<html>
  <body>
    <h1>Qastia Detector</h1>
    <p>
      <form>
        <input Type="button" value="Reshooter" onClick="history.go(0)">
      </form>
    </p>
    <p>Distance: {distance.get_distance()}</p>
    <img src="/shoot">
  </body>
</html>
  """

@app.route("/distance")
def distance():
  return f"<p>distance {distance.get_distance()}</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)