from flask import Flask
from flask import send_file
import RPi.GPIO as GPIO
import threading
import time
from time import sleep
import cv2



is_blink_requested = False
gpio_led = 4
gpio_echo = 20 
gpio_tri = 21


print("**************** Configuration *************")
print(f"** LED Anode : GPIO_{gpio_led}")
print(f"** Détecteur distance ECHO: GPIO_{gpio_echo}")
print(f"** Détecteur distance TRI : GPIO_{gpio_tri}")
print("********************************************")

def diode_loop():
  while True:
    if is_blink_requested:
      state = GPIO.input(gpio_led)
      print(f"Etat de la diode: {state}")

      if state == 0:
        GPIO.output(gpio_led, GPIO.HIGH)
      else:
        GPIO.output(gpio_led, GPIO.LOW)
    time.sleep(1)

threading.Thread(target=diode_loop).start()

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_led, GPIO.OUT)


# Image annotatrion

#This is to pull the information about what each object is called
classNames = []
classFile = "/home/pi/tools/Object_Detection_Files/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

#This is to pull the information about what each object should look like
configPath = "/home/pi/tools/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/pi/tools/Object_Detection_Files/frozen_inference_graph.pb"

#This is some set up values to get good results
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#This is to set up what the drawn box size/colour is and the font/size/colour of the name tag and confidence label
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
#Below has been commented out, if you want to print each sighting of an object to the console you can uncomment below
#print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo



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
  cap = cv2.VideoCapture(0)
  cap.set(3,640)
  cap.set(4,480)
  filename = "/home/pi/data/test_annotated.jpeg"

  success, img = cap.read()
  result, objectInfo = getObjects(img,0.50,0.2)
  print(objectInfo)
  cv2.imwrite(filename, result)
  return send_file(filename, mimetype='image/jpg')


@app.route("/")
def web():
  return """
<html>
  <body>
    <h1>Qastia Detector</h1>
    <form>
      <input Type="button" value="Reshooter" onClick="history.go(0)">
    </form>
    <img src="/shoot">
  </body>
</html>
  """

@app.route("/distance")
  return "<p>distance!</p>"

 GPIO.setmode(GPIO.BCM)

 gpio_tri = 21          # Entree Trig du HC-SR04 branchee au GPIO 21
 gpio_echo  = 20         # Sortie Echo du HC-SR04 branchee au GPIO 20

 GPIO.setup(gpio_tri,GPIO.OUT)
 GPIO.setup(gpio_echo,GPIO.IN)

 GPIO.output(gpio_tri, False)

 repet = input("Entrez un nombre de repetitions de mesure : 1 ")

 for x in range(int(repet)):    # On prend la mesure "repet" fois

    time.sleep(1)       # On la prend toute les 1 seconde

    GPIO.output(gpio_tri, True)
    time.sleep(0.00001)
    GPIO.output(gpio_tri, False)

    while GPIO.input(gpio_echo)==0:  ## Emission de l'ultrason
      debutImpulsion = time.time()

    while GPIO.input(gpio_echo)==1:   ## Retour de l'Echo
      finImpulsion = time.time()

    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

    print(f"La distance est de : {str(distance)}cm")

 GPIO.cleanup()


