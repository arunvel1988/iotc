import time


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)



GPIO.setwarnings(False)

#gnd = ping 6
#output = pin 7
GPIO.output(4, GPIO.OUT)

GPIO.output(4, True)

time.sleep(10)
GPIO.output(4, False)

time.sleep(1)


GPIO.cleanup()
