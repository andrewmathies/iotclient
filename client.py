#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time
import json
import binascii

def on_message(client, userdata, message):
    print(message.timestamp)
    print(message.topic)
    for s in message.payload: 
        print(binascii.b2a_qp(s))
    # print "received a message"
    # print data.length()
    # print("Message Received", message.payload)
    # print("message topic =",message.topic)
    # print("message qos=",message.qos)
     #print("message retain flag=",message.retain)

# broker_address = "test.mosquitto.org" 
# broker_address = "18.221.88.223" 
broker_address = "pivot.iuiot.org" 
client = mqtt.Client("P1")
client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.subscribe("#")
time.sleep(30)
client.loop_stop()

