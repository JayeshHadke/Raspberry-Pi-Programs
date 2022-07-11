# Connect GND - GND, Vcc - Vcc, TRG - GPIO4, ECHO - GPIO18

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 4
echo = 18

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(trig, GPIO.LOW)

start = time.time()
end = time.time()

while GPIO.input(echo) == False:
    start = time.time()

while GPIO.input(echo) == True:
    end = time.time()

sig_time = end-start
dist = sig_time/0.000058

print("Distance {} ".format(dist))
