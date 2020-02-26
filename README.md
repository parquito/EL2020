# Mail_IP

This is a simple Python script to email or text the IP of the Pi to you every time the Pi boots.  In order to use this place the mail_ip.py python script wherever you keep your executable scripts (on my Pi is it in the ~/bin folder.  This folder's path has been exported in my .bashrc.

In order to use this script as intended you must:

**Attain an app password from Google for gmail so the script can use the smtp server:**

*Go to my.account.google.com/security , and click on the "app passwords section"
*Select the app "mail" in this case, and click "generate"
*Copy or save the password to use later in the Python script

**Modify the mail_ip.py script:**

*Change eFROM variable to your gmail address
*Change eTO to the address you want to send the email to. If you want to receive the email as a
text message, you need to send it to an email to sms gateway. These gateways are maintained
by your cell phone provider, and serve as a really easy way to integrate sending a text message
in your scripts. The general format is that the phone number to send the text to is the user and
the gateway is after the @. So for instance, if you have a Verizon cell phone and your number is
(845) 123-4567 then you would send the email to: 8451234567@vtext.com. The following is a
list of gateways for various providers:
	
	Verizon: 1234567890@vtext.com
	T-Mobile: 1234567890@tmomail.net
	AT&T: 1234567890@txt.att.net
	Sprint: 1234567890@messaging.sprint.com
	Google Fi: 1234567890@msg.fi.google.com
	Virgin Mobile: 1234567890@vmobl.com
	Boost Mobile: 1234567890@myboostmobile.com
	Cricket Wireless: 1234567890@mms.cricketwireless.net 

*On line 30 of the script after ‘server.login’ you will need to change the two arguments to your
gmail address, and the app password you set up at the beginning of the assignment.

*Once that is all finished, save your changes, and transfer the file to the Pi. You can put it on a
USB drive and transfer it that way, use the scp command as described in the link I provided
under the “Bash Shell Intro” topic in the Google Classroom, you can even use an sftp client like
Filezilla to transfer the script over. If you are a masochist, you could even just manually type the
script out and save the file as mail_ip.py Whatever works for you.

*However you go about it, put the mail_ip.py script in the ~/bin folder. For good measure we are
going to make it executable:  **sudo chmod +x mail_ip.py**

*Now we are going to test out the script. If everything goes well, it should text you the IP of the
Pi. If it doesn’t work, it will spit an error, and let you know what line the script hangs on: **python mail_ip.py**

*If that all went well, then the last step is to make the script run at boot. We are going to do this
by calling it from the rc.local This is a file that executes during the boot process. Modifying it
will allow us to call the script at that time. We need root privileges to edit this file: **sudo nano /etc/rc.local**

*At the end of this file you will see: “exit 0” It is very important not to put anything after that line.
To call the script, we are going to add 2 lines above it:

**sleep 20**
**python /home/josh/bin/mail_ip.py**

*Make sure to change “josh” to whatever your user name is. Also make sure that you put the
mail_ip.py file in that bin folder. The “sleep 20” is to give the Pi enough time to enable the wifi,
and get on the network before the script is called. If the script is called before the networking
drivers load, the entire script crashes and burns because you can’t use the socket library if there
are no sockets to manipulate. The second line just calls the script with the python interpreter.
Notice that we did not have a shebang at the beginning of our python script. Without the
shebang, you need to tell the operating system what it needs to use to execute the script.

*Hit Ctrl+x and follow the prompts to save and exit out of nano. Then reboot the Pi: **sudo reboot -n**

If all went well, the Pi sill boot, and text you its IP address so you can ssh into it!

