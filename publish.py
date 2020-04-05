#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time 

# broker_address = "18.221.88.223" 
broker_address = "pivot.iuiot.org" 
client = mqtt.Client("P2")
# client.on_message=on_message
client.connect(broker_address)
client.loop_start()
client.publish("bhimebau", 5)
# time.sleep(30)
client.loop_stop()
