#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Waiting for you to scan an RFID sticker/card")
    id = reader.read()[0]
    print("The ID for this card is:", id)
#uses the RFID scanner to scan the value of the card, which is then attatched with a specific playlist/track/album on spotify
    
finally:
        GPIO.cleanup()
