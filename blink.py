import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)

for i in range(3):
	blinkOnce(21)

GPIO.cleanup()
