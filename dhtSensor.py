# git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# or
# download https://github.com/adafruit/Adafruit_CircuitPython_DHT
#           unzip(Extract here) a file in a folder and do
#               > sudo apt-get setup.py install


import Adafruit_DHT
# import sys

# connect DHT11 middle leg with GPIO4 and Connect Vcc and Gnd Accordingly

while True:
    hum, temp = Adafruit_DHT.read_retry(11, 4)
    print("temperature {} and  humidity {} \n".format(temp, hum))
