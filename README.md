# electrobrain
## Introduction
I've been leading a workshop on beginning programming, Rasperry Pi using Python, and Arduino.  The ages of the participants has ranged from 8 years old, (he's 9 now,) to adult.  This project aims to be a set of programs that are simple, but not simplistic, that do interesting things with the Pi and especially its GPIO pins. 

The original program in this group is a status indicator that I made for my RPi3, which lives under a glass dome, [http://imgur.com/3HmyNV5](http://imgur.com/3HmyNV5) as well as for the web server of waycoolbeans.com, which lives in a glass head. 

I've also added a few other python scripts that explore the GPIO output pins. Throughout, I use Broadcom numbering in my code. You'll see it declared as: `GPIO.setmode(GPIO.BCM) `
##led.py
###Usage:
From a command line, run the following command:

`python led.py`


(May be called "`_led.py`" in the repository. It can be safely renamed or run as is.)

### Script details
A python script to creatively illuminate "LED copper wire" lights using the Raspberry Pi's PWM GPIO pins. (As the Pi will live inside a head-shaped glass jar, it got the name "electrobrain")
Quick and crappy video may be available [here] (https://www.facebook.com/mmdc.net/videos/979343528845213/) but I'm not sure if my Facebook settings will allow you to see it.
[image](electrobrain.jpeg)
I'm starting out with a script by Alex Eames (http://RasPi.tv) that I found for working with PWM on the Raspberry Pi
	see: http://RasPi.tv/2013/how-to-use-soft-pwm-in-rpi-gpio-pt-2-led-dimming-and-motor-speed-control 
The script is a simple way to incrementally dim and brighten an LED that's attached to (and powered by)the Pi's PWM-capable GPIO pins.

The original demo I saw used a simple LED, but I recently happened upon some "[LED Copper Wire](http://www.ebay.com/itm/Warm-White-Battery-Powered-100LEDs-Copper-Wire-Xmas-Party-String-Fairy-Light-10M-/141768650258?hash=item210211ee12:g:K68AAOSwQPlV7khq)" strings in a shop and bought them on impulse, knowing I might do something cool with them.  They're made from a pair of very thin strands of varnished wire with tiny surface-mount LEDs attached every few inches, with a blob of some sort of resin covering each LED, which both protects the LED and acts like a diffuser. The strings can be cut to desired lengths.

Strobing the LED strands has a very pleasing effect. The wires have just a bit of stiffness, so they are easy to form and keep their shape a bit.

The glass head we are using is the kind commonly used as a hat stand or for sunglasses.  A quick eBay search is [here](http://www.ebay.com/sch/i.html?_odkw=hollow+glass+head&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xhollow+glass+mannequin+head.TRS0&_nkw=hollow+glass+mannequin+head&_sacat=0).


The goal of this project is to combine several strands of lights to make a passive informational display. So far, I've gotten it to watch system load and have the lights go nuts when the load gets high.

##morse_code.py
### Usage:
From a command line, run the following command:

`python morse_code.py`

### Script details
DJ, our 9 year old inventor and I both have a certain fascination with telegraphy and morse code, so I found a script from Cambridge University that converts text to code, then blinks out the message in Morse.  

The original is [here](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py) And is licensed under a Creative Commons 3 Share Alike license.

This script, when run, simply prompts the user for a string of text, thich it then flashes out on a GPIO pin.

## MessageBlinker.py
### Usage:
From a command line, run the following command:

`python MessageBlinker.py`

### Script details
This script is a bit different—it listens to an MQTT server for an incoming message on the topic you specify at runtime.  When it receives a message, it does a triple-blink on two GPIO pins (BCM 24 & 25) and prints out the message to the terminal:

	(The first time you run it, you'll first want to install the MQTT python library with:
	
	`sudo pip install paho-mqtt`
	
	That's a one-time operation.)

`python MessageBlinker.py`

`Connected with result code 0`

`Type a topic/channel:`

**`test/abcd`** (<-- Your input)

At this point, you can open another terminal, even on a different machine and install some MQTT tools:

`sudo apt-get install -y mosquitto-clients`

Then try:

`mosquitto_pub -h iot.eclipse.org -t "test/abcd" -m "Hello World"`

(This uses a public MQTT server located at iot.eclipse.org.)

## makermorse.py
### Usage:
From a command line, run the following command:

`python makermorse.py.py`

(The first time you run it, you'll first want to install the MQTT python library with:
	
	`sudo pip install paho-mqtt`

### Script details

This script listens to an MQTT topic and converts messages received to Morse code.  
The message is then flashed 
By default, it listens to the topic "test/abcd" on the public MQTT server iot.eclipse.org. (Thes values are easily changed in the script.)
