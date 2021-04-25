from bs4 import BeautifulSoup
import requests
import re
import os
import json
from billboardapi import *

def rap(songs):
    url = 'https://music.apple.com/us/playlist/rap-life/pl.abe8ba42278f4ef490e3a9fc5ec8e8c5'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break

    return l

def pop(songs):
    url = 'https://music.apple.com/us/playlist/todays-hits/pl.f4d106fed2bd41149aaacabb233eb5eb'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break
    return l


def rock(songs):
    url = 'https://music.apple.com/us/playlist/alt-pop/pl.cac8c8af1a654268973929161aba9e33'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break
    return l


def dance(songs):
    url = 'https://music.apple.com/us/playlist/edm-hits/pl.d66feecbd40d423d81e8e643e368291a'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break
    return l

def country(songs):
    url = 'https://music.apple.com/us/playlist/todays-country/pl.87bb5b36a9bd49db8c975607452bfa2b'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break
    return l


def latin(songs):
    url = 'https://music.apple.com/us/playlist/dale-play/pl.4b364b8b182f4115acbf6deb83bd5222'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='row track web-preview song')
    l = []
    for title in songs:
        for row in rows:
            song = row.find('div', {'tabindex' : '-1'})
            name = str(song.text).strip().replace('’', '')
            search = title[0].replace("'", "")      
            if name.lower().find(search.lower()) != -1:
                time = row.find('div', class_='time-data').text
                time = time.strip()
                l.append((title[0], title[1], time))
                break
    return l


def get_data(d):
    data = {}
    data['Rap'] = rap(d['rap'])
    data['Pop'] = pop(d['pop'])
    data['Rock'] = rock(d['rock'])
    data['Dance'] = dance(d['dance'])
    data['Country'] = country(d['country'])
    data['Latin'] = latin(d['latin'])
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




