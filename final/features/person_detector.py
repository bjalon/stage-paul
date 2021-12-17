from datetime import datetime
from time import sleep
import threading

from os import listdir
from os.path import isfile, join

import ia

DATA_DIR = "/home/pi/data/persons"


def person() :
 while True
  time.sleep(60)
  cap = cv2.VideoCapture(0)
  cap.set(3,640)
  cap.set(4,480)
  success, img = cap.read()

  result, objectInfo = ia.getObjects(img,0.50,0.2)

  if "person" in str(objectInfo):
    filename = datetime.now().strftime(f"{DATA_DIR}/%Y%m%d %H%M%S.jpg")
    print(f"une personne a été trouvée, enregistrement dans {filename}")
    cv2.imwrite(filename, result)

def get_persons_files():
    return [f for f in listdir(DATA_DIR) if isfile(join(DATA_DIR, f)) and f.endswith(".jpg")]
    list_persons = ""
    for file in files:
      list_persons = list_persons + "hskdfjh" + file + "dskjfsldkj"


threading.Thread(target=person).start()

def generate_html():
  list_persons = """
  <html>
   <body>
    <ul>"""

  files = get_persons_files()
  for file in files:
    list_persons = list_persons + "    <li><a href=\"/home/pi/data/persons/" + file + "\">" + file + "</a></li>\n"

  list_persons = list_persons + """  </ul>
   </body>
  </html>
   """
   return list_persons
