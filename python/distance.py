import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print( "+-----------------------------------------------------------+")
print( "|   Mesure de distance par le capteur ultrasonore HC-SR04   |")
print( "+-----------------------------------------------------------+")

gpio_tri = 21          # Entree Trig du HC-SR04 branchee au GPIO 21
gpio_echo  = 20         # Sortie Echo du HC-SR04 branchee au GPIO 20

GPIO.setup(gpio_tri,GPIO.OUT)
GPIO.setup(gpio_echo,GPIO.IN)

GPIO.output(gpio_tri, False)

repet = input("Entrez un nombre de repetitions de mesure : ")

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
