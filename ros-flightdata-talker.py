import time

import roslibpy
from roslibpy import Message

client = roslibpy.Ros(host='localhost', port=9090)
talker = roslibpy.Topic(client, '/flightdata', 'flightdata/att')


def start_talking():
    while client.is_connected:
        talker.publish(roslibpy.Message({'roll': 21.0, 'pitch': 22.0, 'yaw': 21.0}))
        print('Sending message...')
        time.sleep(1)


    #Unregister as a publisher for the topic
    talker.unadvertise()

#Add a callback to be executed when the connection is established.
client.on_ready(start_talking)
#Kick-starts a blocking loop to wait for events.
client.run_forever()
