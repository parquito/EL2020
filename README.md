# EL2020
You will need a Raspberry pi, GPIO extension board, a breadboard, a buzzer sensor, and at least one smoke detector (MQ2,MQ5,MQ7,Flame Detector)

You must make sure you have the following installed: -Python3 -SQLite3 -Python pip, after pip is installed, install flask

First off, hook up your sensors and test to make sure they work. The buzzer sensor is an ouput, ran like an LED, and the smoke sensors are digital input. It is read when a certain threshold is passed. You set that threshold with the screw on the sensor.

Next, you need to make a python script to log the times your sensors are set off in a comma-seperated values (.csv) file. You should also log the time 30 seconds after it is set off using deltatime operations. Then create an SQL database based off of your csv file.

Next, you will need to make a python flask server to use you sql database info and serve an html file. Create a new directory called templates and create a file called index.html inside. index.html will display information from the flask server which gets it's info from the sql database.

Here is an example of my breadboard correctly wired and a demonstration of the smoke detector:
