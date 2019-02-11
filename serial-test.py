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
    att=line.split(" ")
    #print(len(att))
    print("roll: "+att[0]+"   pitch: "+att[1]+"   roll: "+att[2])

# close port 
ser.close() 
