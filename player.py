#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"

#IDs from spotify
CLIENT_ID="c8f6be65e48d44d2b20ddf44cc248b7d"
CLIENT_SECRET="c4d93197142a48429280c0133ba6a5ff"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("waiting for record scan")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
    
            # id = " " corresponds to the value of the RFID card
            if (id==1047110430890):
        
                # Harry Potter Soundtrack
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6zeHM5CV0CjcS0K8ouWE4N')
                sleep(4)
        
            elif (id==347334318633):
        
                # Mr. Ben Classical Music
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3LoPqu7BDmZ0YrfMNNgIOv')
                sleep(4)
        
            elif (id==487282255466):
        
                # Views by Drake
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:40GMAhriYJRO1rsY4YdrZb')
                sleep(4)
    except Exception as e:
        print(e)
        pass
    
    finally:
        print("Cleaning up...")
        GPIO.Cleanup()
