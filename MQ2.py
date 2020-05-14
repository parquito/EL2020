import time, sys
import RPi.GPIO as GPIO

#Pin for the MQ2 Smoke Detector
smokePin = 24

#Set up the GPIO BCM mode is how we reference the pins.  This is GPIO 17 If I set it to BOARD, i would have to count the pin numbers
GPIO.setmode(GPIO.BCM)
#This line tells the Pi how to measure the signal that is coming in.
GPIO.setup(smokePin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(smokePin):
	print('Smoke detected!')
	return

#These two lines use changes to the presented voltage to GPIO 17 to trigger an event.  
#The first line sets the trigger (if the voltage is rising) 
#The second line sets the callback for that trigger, in this case calling the function "action"
GPIO.add_event_detect(smokePin, GPIO.RISING)
GPIO.add_event_callback(smokePin, action)

#Sets a while look, checking the sensor every .5 seconds.
try:
	while True:
		print('active')
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
