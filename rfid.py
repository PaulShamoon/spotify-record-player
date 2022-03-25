#!/usr/bin/env python
#Use this script to get the RFID numbers associated with your RFID tag

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
        print("reading...")
        id = reader.read()[0]
        print(id)

finally:
        GPIO.cleanup()