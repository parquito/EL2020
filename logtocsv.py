import RPi.GPIO as GPIO
import time, sys
import os
import datetime
import csv
import smtplib
import socket
import sqlite3 as sql

sensor1 = 17
sensor2 = 22
sensor3 = 27
sensor4 = 24
buzzer = 21

input_state = True
smoke = "clear"

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor3,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensor4,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer,GPIO.OUT)

eFROM = "hsghsghsghsghsghsghsg@gmail.com"
eTO = "6307797109@vtext.com"
Subject = "FIRE"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

eCHK = 0

con = sql.connect('smokeLog.db')
cur = con.cursor()


def buzzer(pin):
	print "buzz"
	for i in range(3):
		GPIO.output(pin,True)
		time.sleep(.5)
		GPIO.output(pin,False)
		time.sleep(1)


def read(pin):
	smoke = "smoke"
	for i in range(10):
		buzzer(buzzer)
	smoke = "clear"

GPIO.add_event_detect(sensor1, GPIO.RISING)
GPIO.add_event_callback(sensor1, read)
GPIO.add_event_detect(sensor2, GPIO.RISING)
GPIO.add_event_callback(sensor2, read)
GPIO.add_event_detect(sensor3, GPIO.RISING)
GPIO.add_event_callback(sensor3, read)
GPIO.add_event_detect(sensor4, GPIO.RISING)
GPIO.add_event_callback(sensor4, read)

try:
	while smoke == "clear":
		time.sleep(5)
		cur.execute('INSERT INTO smokeLog values(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),smoke))
		con.commit()
		table = con.execute("select * from smokeLog")
		os.system('clear')
		print "%-30s %-30s" %("Date/Time", "Smoke")
		for row in table:
			print "%-30s %-30s" %(row[0], row[1])
	while smoke == "smoke":
		cur.execute('INSERT INTO smokeLog values(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),smoke))
		con.commit()
		table = con.execute("select * from smokeLog")
		os.system('clear')
		print "%-30s %-30s" %("Date/Time", "Smoke")
		for row in table:
			print "%-30s %-30s" %(row[0], row[1])
		text = "SMOKE/FLAMMABLE GAS DETECTED IN ROOM"
		eMessage = 'Subject: {\n\n{}'.format(Subject, text)
		server.login("hsghsghsghsghsghsghsg@gmail.com", "gfzx acav aorr ahqo")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit


except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()

finally:
	GPIO.cleanup()
