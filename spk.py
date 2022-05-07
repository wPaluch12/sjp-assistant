#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time
import pyttsx3 as tts
end = None
BROKER = "localhost"

################################################################################
def send(topic, payload):
    global client
client.publish(topic, payload, retain=False) # publish

########################################################################### #####
def on_message(client, userdata, message): global kk
topic = message.topic
payload = str(message.payload.decode("utf-8")) print("rcv", topic, payload) kk.append(payload)

########################################################################### #####
def init():
    global client
# print("creating new instance")
client = mqtt.Client("spk-pc") # create new instance client.on_message = on_message # attach function to callback print("connecting to broker")
client.connect(BROKER) # connect to broker client.loop_start() # start the loop client.subscribe(("cmd/tts/pc", 0))

########################################################################### #####
def loop():
    global kk
    engine = tts.init()
    engine.setProperty('volume', 0.7)
    engine.setProperty('rate', 190)
    kk = []
    while True:
        while len(kk) > 0:
            engine.say(kk.pop(0))
            engine.runAndWait()
            time.sleep(1)
########################################################################### #####
init()
loop()
########################################################################### #####
