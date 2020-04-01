import RPi.GPIO as GPIO
import time

greenPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(greenPin,GPIO.OUT)

def oneBlink(pin):
	i = 1
	while i < 7:
		GPIO.output(pin,True)
		time.sleep(1)
		GPIO.output(pin,False)
		time.sleep(1)
		i += 1

oneBlink(greenPin)

exit()
