import time
import serial
import roslibpy
from roslibpy import Message

client = roslibpy.Ros(host='172.28.229.228', port=9090)
talker = roslibpy.Topic(client, '/flightdata', 'flightdata/att')

ser = serial.Serial('/dev/serial0', 115200, timeout=None)

# check which port was really used
print(ser.name)

def start_talking():
    while client.is_connected:
        line = ser.readline()
        line = line.rstrip()
        # print line
        # print(line)
        att=line.split()

        talker.publish(roslibpy.Message({'roll': int(att[0]), 'pitch': int(att[1]), 'yaw': int(att[2])}))
        print('Sending message...')
        #time.sleep(1)
    #Unregister as a publisher for the topic
    talker.unadvertise()

#Add a callback to be executed when the connection is established.
client.on_ready(start_talking)
#Kick-starts a blocking loop to wait for events.
client.run_forever()
                                
