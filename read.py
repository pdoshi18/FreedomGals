#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
#This was initally used to find the RFID card values so we could finalize the code but now is an extra precaution to check if card scanned properly
try:
    print("Waiting for RFID card")
    id = reader.read()[0]
    print("The ID for this card is:", id)
#uses the RFID scanner to scan the value of the card, which is then attatched with a specific playlist/track/album on spotify
    
finally:
        GPIO.cleanup()
