import os
import time
import smtplib
import socket

Text = ""

#SMTP Variables
eFROM = "<user@gmail.com>"
eTO = "<phone#>@<sms gateway address>"
Subject = "IP Address of Pi"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#Function to determine IP address, and return it:
def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		#The IP address below doesn't even have to be reachable, it just needs to attempt to reach it
		s.connect(('172.217.9.228', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

Text = get_ip()

print "Your IP Address is " + Text
print "Sending Text Message Now"

eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
server.login("<user>@gmail.com", "<app password>")
server.sendmail(eFROM, eTO, eMessage)
server.quit
time.sleep(5)

