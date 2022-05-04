#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="c8f6be65e48d44d2b20ddf44cc248b7d"
CLIENT_SECRET="c4d93197142a48429280c0133ba6a5ff"

# Spotify Authentication, all info is specific to our group's spotify account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080",
                                               scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberri Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:45vW6Apg3QwawKzBi03rgD'])
