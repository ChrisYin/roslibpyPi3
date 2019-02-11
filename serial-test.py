import serial

# open serial port                                                                  
ser = serial.Serial('/dev/serial0', 115200, timeout=None)
# check which port was really used
print(ser.name)                                                           

while 1 :
    # read a '\n' terminated line
    line = ser.readline()
    line = line.rstrip()
    # print line
    # print(line)
    att=line.split()
    #print(len(att))
    print("roll: %f"%(float(att[0]))+"  pitch: %f"%(float(att[1]))+"  yaw: %f"%(float(att[2])))

# close port 
ser.close() 
