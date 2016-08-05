# Adapted from https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py
# Certain values have been adjusted to make the timings better
# TODO: Add functionality to adjust the WPM rate 
# TODO: Smooth out the timings more, as it doesn't blink 'naturally'

import RPi.GPIO as GPIO
import time


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
ledPin=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


def dot():
	GPIO.output(ledPin,1)
	time.sleep(0.1)
	GPIO.output(ledPin,0)
	time.sleep(0.1)

def dash():
	GPIO.output(ledPin,1)
	time.sleep(0.3)
	GPIO.output(ledPin,0)
	time.sleep(0.3)

while True:
	input = raw_input('What would you like to send? ')
	for letter in input:
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				else:
					time.sleep(0.5)
			time.sleep(0.5)
