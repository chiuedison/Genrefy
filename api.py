import unittest
import json
import os
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_client_id = 'da054f40b6a24c86bd8b3ac35d39ca64'
spotify_client_secret = '39958d8b03574cebb226082b59ae0068'

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])