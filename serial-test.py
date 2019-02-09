import serial

# open serial port                                                                  
ser = serial.Serial('/dev/serial0', 115200, timeout=None)
# check which port was really used
print(ser.name)                                                           

while 1 :
    # read a '\n' terminated line
    line = ser.readline()
    # print line
    print(line),                                                                                                      

# close port 
ser.close() 
