import requests
import json
import unittest

def web_songs(songs):

    title_artist_list = []

    for song in songs:
        title = song[0]
        artist = song[1]

        feed = get_lyrics(title, artist)
        title_artist_list.append(feed)

    return title_artist_list

def get_lyrics(title, artist):
    name = artist
    if artist.find('Featuring') != -1:
        name = artist.split('Featuring')[0]
    elif artist.find('&') != -1:
        name = artist.split('&')[0]
    elif artist.find(' X ') != -1:
        name = artist.split(' X ')[0]
    elif artist.find(',') != -1:
        name = artist.split(',')[0]
    elif artist.find('(') != -1:
        name = artist.split('(')[0]
    elif artist.find('+') != -1 and artist != 'Dan + Shay':
        name = artist.split('+')[0]
    elif artist.find('Duet') != -1:
        name = artist.split('Duet')[0]
    elif artist.find('With') != -1:
        name = artist.split('With')[0]
    
    base_url = "https://api.lyrics.ovh/v1/{}/{}"
    request_url = base_url.format(name, title)

    r = requests.get(request_url)
    data = r.text
    #print(data)
    lst = json.loads(data)
    #print(lst)
    lyrics = lst['lyrics']
    #print(lyrics.split())
    word_count = len(lyrics.split())
    return (title, name, word_count)
    