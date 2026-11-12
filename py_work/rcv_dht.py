import serial
#from time import sleep
sp = serial.Serial(port='COM3', baudrate=9600,timeout=1)
while True:
    if sp.readable():
        rcv = sp.readline()
        if(rcv.decode()[0:4]=="humi"):
            humi = int(rcv.decode()[4:6])
            print(humi)
        if rcv.decode()[0:4]=="temp":
            temp = int(rcv.decode()[4:6])
            print(temp)
            print(rcv.decode()[4:6])
        #print(rcv.decode()[:len(rcv)-1])


