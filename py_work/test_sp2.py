import serial
#from time import sleep
sp = serial.Serial(port='COM3', baudrate=9600,timeout=1)
while True:
    if sp.readable():
        rcv = sp.readline()
        print(rcv.decode()[:len(rcv)-1])


