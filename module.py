#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import time
import paho.mqtt.client as mqtt
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging

BROKER = "localhost"
ID = "pc"

########################################################################### #####
def assistant(question):
    words = question.split() #spliting the question by words
    key_word = words[-1] #last word that we want to know the meaning
    ask = question.rsplit(' ', 1)[0] #question without a word that we are looking for meaning
    
    #function that returns meaning of the word
    def get_definition(word):
      url = 'http://sjp.pl/' + parse.quote(word) #creating an url to the sjp.pl website with the key word
      try:
        html = urlopen(url).read() #saving the html code of the page
      except:
        print("[Error] Can't connect to the service") #error when we cant reacg the website
        sys.exit(2)
      soup = BeautifulSoup(html)
      
      # if there is a definition of this word in sjp dictionary:
      ex = soup.find_all('p', style="margin: .5em 0; font: medium/1.4 sans-serif; max-width: 34em; ") #definiction of key word
      
      #if there isn't a definition of this word in sjp dictionary:
      if not ex:
      return "nie znaleziono szukanego słowa w słowniku"
      ex = ex[0]
      return ex.contents[0::2] #return the definition
      
    definition = get_definition(key_word)
    if ask in [
        'co oznacza', 'znaczenie słowa', 'co znaczy słowo', 'jakie jest znaczenie słowa', 'co to', 'co znaczy', 
        'co oznacza słowo', 'jaki jest znaczenie słowa', 'kto to', 'kim jest','jakie znaczenie ma słowo','jakie znaczenie ma'
        ]:
    if definition == "nie znaleziono szukanego słowa w słowniku":
      return "nie znaleziono szukanego słowa w słowniku" 
    else:
      return f'Słowo {slowo} oznacza: {definicja}' 
      
    return 'Proszę powtórzyć pytanie'
    
########################################################################### #####
def send(topic, payload):
    global client
    print("snd", topic, payload)
    client.publish(topic, payload, retain=False) # publish 

########################################################################### #####
def on_message(client, userdata, message):
    topic = message.topic
    payload = str(message.payload.decode("utf-8"))
    print("rcv", topic, payload)
    odp = asystent(payload.lower())
    logging.basicConfig(level=logging.DEBUG, filename="logi.log", filemode="a")
    logging.debug("Pytanie: {}".format(payload) + "\n \t Odpowiedź: {}".format(odp))
        if odp is not None:
    send("cmd/tts/" + ID, odp)

########################################################################### #####
def init():
    global client
    # print("creating new instance")
    client = mqtt.Client(ID) # create new instance 
    client.on_message = on_message # attach function to callback 
    # print("connecting to broker")
    client.connect(BROKER) # connect to broker 
    client.loop_start() # start the loop 
    client.subscribe(("sig/stt/#", 0))

########################################################################### #####
def loop():
    while True:
        time.sleep(60)

###########################################################################
#####
init()
loop()
########################################################################### #####
