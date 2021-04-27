import requests
import json
import unittest

def web_songs(songs):

    title_artist_list = []

    for song in songs:
        title = song[0]
        artist = song[1]

        feed = get_lyrics(title, artist)
        title_artist_list.append((feed[0], feed[1], song[2], feed[2]))

    return title_artist_list

def get_lyrics(title, artist):
    name = artist
    if name.find('Featuring') != -1:
        name = name.split(' Featuring')[0]
    if name.find('&') != -1:
        name = name.split(' & ')[0]
    if name.find(' X ') != -1:
        name = name.split(' X ')[0]
    if name.find(' x ') != -1:
        name = name.split(' x ')[0]
    if name.find(',') != -1:
        name = name.split(',')[0]
    if name.find('(') != -1:
        name = name.split('(')[0]
    if name.find('+') != -1 and artist != 'Dan + Shay':
        name = name.split(' + ')[0]
    if name.find('Duet') != -1:
        name = name.split(' Duet')[0]
    if name.find('With') != -1:
        name = name.split(' With')[0]

    
    base_url = "https://api.lyrics.ovh/v1/{}/{}"
    request_url = base_url.format(name, title)

    r = requests.get(request_url)
    data = r.text
    #print(data)
    lst = json.loads(data)
    if 'error' in lst.keys():
        return (title, artist, 0)
    #print(lst)
    lyrics = lst['lyrics']
    #print(lyrics.split())
    word_count = len(lyrics.split())
    return (title, artist, word_count)
    