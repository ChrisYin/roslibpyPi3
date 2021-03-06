import time

import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')


def start_talking():
    while client.is_connected:
        talker.publish(roslibpy.Message({'data': 'Hello World!'}))
        print('Sending message...')
        time.sleep(1)


    #Unregister as a publisher for the topic
    talker.unadvertise()

#Add a callback to be executed when the connection is established.
client.on_ready(start_talking)
#Kick-starts a blocking loop to wait for events.
client.run_forever()
