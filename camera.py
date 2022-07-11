# sudo apt-get install python_picamera
# sudo apt-get install python3_picamera

# sudo raspi-config
# interface option -> Enable cmaera

# restart --now


import picamera
import time

camera = picamera.PiCamera()
camera.capture('exam.jpg')

camera.vflip(true)

camera.capture('exam2.jpg')

camera.start_recording('examvid.h264')
tinme.sleep(5)
camera.stop_recording()
