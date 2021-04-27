from bs4 import BeautifulSoup
import requests
import re
import os
import json
from billboardapi import *

def get_song_lengths(songs, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='songs-list-row songs-list-row--web-preview web-preview songs-list-row--two-lines songs-list-row--song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='songs-list-row__length').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break

    return l


def get_data(d):
    data = {}
    data['Rap'] = get_song_lengths(d['rap'],'https://music.apple.com/us/playlist/rap-life/pl.abe8ba42278f4ef490e3a9fc5ec8e8c5')
    data['Pop'] = get_song_lengths(d['pop'], 'https://music.apple.com/us/playlist/todays-hits/pl.f4d106fed2bd41149aaacabb233eb5eb')
    data['Rock'] = get_song_lengths(d['rock'], 'https://music.apple.com/us/playlist/alt-pop/pl.cac8c8af1a654268973929161aba9e33')
    data['Dance'] = get_song_lengths(d['dance'], 'https://music.apple.com/us/playlist/edm-hits/pl.d66feecbd40d423d81e8e643e368291a')
    data['Country'] = get_song_lengths(d['country'], 'https://music.apple.com/us/playlist/todays-country/pl.87bb5b36a9bd49db8c975607452bfa2b')
    data['Latin'] = get_song_lengths(d['latin'], 'https://music.apple.com/us/playlist/dale-play/pl.4b364b8b182f4115acbf6deb83bd5222')
    return data

def unique_songs(d):
    unique = []
    ret = []
    songs = []
    for category in d:
        for song in d[category]:
            if song not in unique:
                tup = (song[0], song[1], category, song[2])
                songs.append(tup)
                unique.append(song)

    return songs


'''
url = 'https://api.lyrics.ovh/v1/Lil-Baby/On-Me'
r = requests.get(url)
d = json.loads(r.content)
lyrics = d['lyrics']
lyrics_list = lyrics.split()
count = 0
for word in lyrics_list:
    count += 1

print(count)'''




