import serial
import time
from os.path import join

        
path="/home/jonas/Schreibtisch"
ser = serial.Serial(
    port='/dev/ttyS0',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=5)
file= open(join(path,"Daten.txt"),'w')
file= open(join(path,"Daten.txt"),'a')
file.write("x")
file.write(";")
file.write("y")
file.write("\n")
file.close
    

while True:
    x=ser.readline()
    x=str(x.decode("utf-8"))
    print(x)
    x=str(x)
    file= open(join(path,"Daten.txt"),'a')
    file.write(x)
    file.write("\n")
    file.close
    
    
    

ser.close()
