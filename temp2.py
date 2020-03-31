import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import datetime
import csv
import smtplib
import socket
import sqlite3 as sql

redPin = 27
greenPin = 22
tempPin = 17

input_state = True

tempSensor = Adafruit_DHT.DHT11
blinkDur = .1
blinkTime = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

eFROM = "hsghsghsghsghsghsghsg@gmail.com"
eTO = "6307797109@txt.att.net"
Subject = "temperature out of range"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

eCHK = 0

#connect db
con = sql.connect('tempLog.db')
cur = con.cursor()

### this will do it to greenPin if greenPin is sent to oneBlink
def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin, False)
	time.sleep(blinkDur)

def alert(tempF):
	global eCHK
	if eCHK == 0:
		Text = "The monitor now indicates that the temperature is now "+str(tempF)
		eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
		server.login("hsghsghsghsghsghsghsg@gmail.com", "gfzx acav aorr ahqo")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eCHK = 1

def readDHT(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempF = '{0:0.1f}'.format(temperature)
		humid = '{1:0.1f}'.format(temperature, humidity)
	else:
		print('Error Reading Sensor')
	return tempF, humid

#def readH(tempPin):
#	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
#	if humidity is not None and temperature is not None:
#		humPer = '{1:0.1f}%'.format(humidity)
#	else:
#		print('Error Reading Sensor')
#	return humPer

oldTime = 60
tempF, hum = readDHT(tempPin)

### READ TEMP AND HUMIDITY FIRST, THEN ACTIVATE THE PIN
try:
	while True :
		if 70 <= float(tempF) <= 80:
			eCHK = 0
			GPIO.output(redPin, False)
			GPIO.output(greenPin, True)
		else:
			GPIO.output(greenPin, False)
			alert(tempF)
			oneBlink(redPin)

		if time.time() - oldTime > 59:
			tempF, humid = readDHT(tempPin)
			print(tempF,humid)

#			cur.execute('INSERT INTO tempLog values(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),tempF, humid))
			cur.execute('INSERT INTO tempLog values(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'), tempF))
			con.commit()
			table = con.execute("select * from tempLog limit 5")
			os.system('clear')
#			print "%-30s %-20s %-20s" %("Date/Time", "Temp", "Humidity")
			print "%-30s %-20s" %("Date/Time", "Temp")
			for row in table:
#				print "%-30s %-20s %-20s" %(row[0], row[1], row[2])
				print "%-30s %-20s" %(row[0], row[1])
			oldTime = time.time()
except KeyboardInterrupt:
		os.system('clear')
		con.close()


### WHERE I LEFT OFF

#
#3			date = datetime.datetime.now()
#			temp = readF(tempPin)
#			humi = readH(tempPin)

#			if temperature > 70.0 and temperature < 80.0:
##				GPIO.output(greenPin, True)
#			else:
#				oneBlink(redPin)
#				text = readF(tempPin)
#				server.login("hsghsghsghsghsghsghsg@gmail.com", "gfzx acav aorr ahqo")
#				eMessage = 'Subject: {}\n\n{}'.format(subject, text)
#				server.sendmail(eFROM, eTO, eMessage)
#				server.quit
#				time.sleep(5)
#use "a" to appened instead of overwrite
#			f= open("templog.csv", "a")
#			wc = csv.writer(f)
#			wc.writerow([date,temp])

#			time.sleep(60)
#			infiniteloop += 1

#except KeyboardInterrupt:
#	f.close()
#	os.system('clear')
#	print('Thanks for Blinking and Thinking!')
#	GPIO.cleanup()
