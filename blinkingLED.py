# connect LED long leg to GPIO4 and short with GND
import RPi.GPIO as GPIO
import time

pin = 4
GPIO.setMode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

for i in range(40):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(pin, GPIO.LOW)


GPIO.cleanup()
GPIO.setwarnings(False)
