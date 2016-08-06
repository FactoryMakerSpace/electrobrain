#! /usr/bin/env python2.7

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # always needed with RPi.GPIO
from time import sleep  # pull in the sleep function from time module
import time as time

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(25, GPIO.OUT)# set GPIO 25 as output for white led
GPIO.setup(24, GPIO.OUT)# set GPIO 25 as output for white led

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
ledPin = 25

def dot():
    # print(".")
    GPIO.output(ledPin,1)
    time.sleep(0.1)
    GPIO.output(ledPin,0)
    time.sleep(0.1)

def dash():
    # print("_")
    GPIO.output(ledPin,1)
    time.sleep(0.3)
    GPIO.output(ledPin,0)
    time.sleep(0.1)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/abcd")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    input = str(msg.payload)
    print(input)
    for letter in input:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.3)
            time.sleep(0.5)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
