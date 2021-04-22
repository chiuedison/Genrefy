from bs4 import BeautifulSoup
import requests
import re
import os

url = 'https://www.billboard.com/charts/dance-electronic-songs'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup)