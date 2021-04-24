from bs4 import BeautifulSoup
import requests
import re
import os
import json

url = 'https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
rows = soup.find_all('div', class_='row track web-preview song')

time = rows.text.strip()
print(r)




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




