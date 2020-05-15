
import RPi.GPIO as GPIO
import time, sys
import os
import smtplib
import sqlite3 as sql

smokePin = 27
buzzpin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(smokePin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzpin,GPIO.OUT)

eFROM = "hsghsghsghsghsghsghsg@gmail.com"
eTO = "6307797109@vtext.com"
Subject = "FIRE"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smokeCHK = 0
GPIO.output(buzzpin,True)

def buzzer(pin):
	print "buzz"
	for i in range(3):
		GPIO.output(pin,True)
		time.sleep(.5)
		GPIO.output(pin,False)
		time.sleep(1)

def readSmoke(pin):
	if smokeCHK == 0:
		con = sql.connect('smokeLog.db')
		cur = con.cursor()
		smoke = "smoke detected"
		for i in range(1):
			buzzer(buzzpin)
		cur.execute('INSERT INTO smokeLog values(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),smoke))
		con.commit()
		table = con.execute("select * from smokeLog")
		os.system('clear')
		print "%-30s %-30s" %("Date", "Smoke")
		for row in table:
			print "%-30s %-30s" %(row[0], row[1])
		text = "SMOKE/FLAMMABLE GAS DETECTED IN ROOM"
		eMessage = 'Subject: {}\n\n{}'.format(Subject, text)
		server.login("hsghsghsghsghsghsghsg@gmail.com", "gfzx acav aorr ahqo")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		con.close()
		smokeCheck = 1
	else:
		print('smoke event ongoing')
def sensoron(pin):
	smokeCHK = 0


GPIO.add_event_detect(smokePin, GPIO.RISING)
GPIO.add_event_callback(smokePin, readSmoke)

try:
	while smokeCHK == 0:
		print('reading sensors...')
		time.sleep(30)
	while smokeCHK == 1:
		GPIO.add_event_detect(smokePin, GPIO.FALLING)
		GPIO.add_event_callback(smokePin, sensoron)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
