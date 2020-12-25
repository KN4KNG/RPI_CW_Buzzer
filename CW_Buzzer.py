#A lot of code taken and inspired from: https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

CODE = {' ': ' ',
        "'": ".----.",
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
        
buzzerPin=8
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

def dot():
        GPIO.output(buzzerPin,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(buzzerPin,GPIO.LOW)
        time.sleep(0.1)

def dash():
        GPIO.output(buzzerPin,GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(buzzerPin,GPIO.LOW)
        time.sleep(0.1)

while True:
        input = raw_input('ENTER MESSAGE TO SEND IN CW: ')
        for letter in input:
                        for symbol in CODE[letter.upper()]:
                                if symbol == '-':
                                        dash()
                                elif symbol == '.':
                                        dot()
                                else:
                                        time.sleep(0.25)
                        time.sleep(0.25)
