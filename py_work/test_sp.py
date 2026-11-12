import serial
from time import sleep
sp = serial.Serial(port='COM3', baudrate=9600,timeout=0)
while True:
    sp.write(b'1')
    sleep(1)
    sp.write(b'0')
    sleep(1)


