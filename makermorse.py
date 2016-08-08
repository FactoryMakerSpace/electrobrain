#! /usr/bin/env python2.7
# -*- coding: iso-8859-15 -*-

# Hacked together by #jimoconnell
# A Python program for the Raspberry Pi to listen
# to an MQTT topic and convert the message to
# Morse code, which is displayed via an LED
# or tapped out on a relay or sounder.
# TODO: Add support for piezo or speaker
# Based upon a Creative Commons Attribution-ShareAlike 3.0 Unported Licensed script located at:
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py

#################################################
#              User Settings

# Set standard Morse timings.
# (You probably only want to change the "dit" value.)
# a 0.05 sec dit is around 26 wpm

dit = 0.05
dah = 3 * dit
lettergap = 3 * dit
wordgap = 7 * dit

# Set which pin you will be connecting LED or sounder to:
# ( BCM Numbering )
signalPin = 25

# Your preferred MQTT Server and topic:
mqttServer = "iot.eclipse.org"
mqttTopic = "test/abcd"

#             End of User Settings
#################################################

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # always needed with RPi.GPIO
from time import sleep  # pull in the sleep function from time module
import time as time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM


# set signalPin (set above) as output for led or sounder
GPIO.setup(signalPin, GPIO.OUT)# set signalPin (set above) as output for led

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

#  Not sure how to include these, as they conflict with letter.upper()
#        'Ä': '.-.-',
#        'Á': '.--.-',
#        'Å': '.--.-',
#        'Ch': ' ----',
#        'É': '..-..',
#        'Ñ': '--.--',
#        'Ö': '---.',
#        'Ü': '..--'}

def dot():
    # print(".")
    GPIO.output(signalPin,1)
    time.sleep(dit)
    GPIO.output(signalPin,0)
    time.sleep(dit)

def dash():
    # print("_")
    GPIO.output(signalPin,1)
    time.sleep(dah)
    GPIO.output(signalPin,0)
    time.sleep(dit)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to:\n\t "+mqttServer+":/"+mqttTopic+"\nwith result code: "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mqttTopic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    input = msg.topic+" "+str(msg.payload)
    input = str(msg.payload)
    print(input)
    for letter in input:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(lettergap)
            time.sleep(wordgap)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqttServer, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
