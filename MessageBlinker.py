#! /usr/bin/env python2.7

# MessageBlinker is a little program that listens to an MQTT channel and 
# blinks a quick pattern when a message is received, then prints the message.

# MQTT is the protocol we use for communicating
import paho.mqtt.client as mqtt

# Rpi.GPIO is the library that lets us talk to the GPIO pins
import RPi.GPIO as GPIO # always needed with RPi.GPIO

# We use sleep(), so let's import it
from time import sleep  # pull in the sleep function from time module

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(25, GPIO.OUT)# set GPIO 25 as output for white led
GPIO.setup(24, GPIO.OUT)# set GPIO 25 as output for white led


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    #Ask the user what topic they want to watch:
    topic = raw_input("Type a topic/channel:\n")
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # Blink some lights when a message is received:
    GPIO.output(25,True)
    sleep(.05)
    GPIO.output(25,False)
    sleep(.1)
    GPIO.output(24,True)
    sleep(.1)
    GPIO.output(24,False)
    sleep(.1)
    GPIO.output(25,True)
    sleep(.05)
    GPIO.output(25,False)

# wait for new messages:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
