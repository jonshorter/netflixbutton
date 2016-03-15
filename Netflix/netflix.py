import RPi.GPIO as GPIO
import time
import subprocess
import shlex

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.OUT)
vpn_state = True

#kill any openvpn service already running
subprocess.call(shlex.split("sudo killall openvpn"), shell=False)

# blinking function  
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(0.03)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(0.03)  
        return  

while True:
	output = subprocess.check_output(['ps', '-A'])
	if 'openvpn' in output:
		GPIO.output(17,GPIO.HIGH)
		vpn_state = True
	else:
		GPIO.output(17,GPIO.LOW)
		vpn_state = False

	input_state = GPIO.input(18)
	if input_state == False:
        	print('Button Pressed')
		if vpn_state == False: 
			cmd = "sudo service openvpn start"
			print "starting openvpn service" 
			subprocess.call(shlex.split(cmd), shell=False)
			for i in range(0,9): blink(17)  
		else:	
			cmd = "sudo service openvpn stop"
			print "stopping openvpn service"
			subprocess.call(shlex.split(cmd), shell=False)
			for i in range(0,9): blink(17)  
#	time.sleep(0.2)

#should never reach here
GPIO.cleanup()   

