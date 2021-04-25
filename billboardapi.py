

import billboard


def test_songs_list(category):
    chart = billboard.ChartData(category)
    l = []
    for entry in chart:
        t = (entry.title.strip(), entry.artist.strip())
        l.append(t)
    return l

def songs_list(category):
    chart = billboard.ChartData(category)
    l = []
    for entry in chart:
        t = (entry.title.strip(), entry.artist.strip())
        l.append(t)
    return l

def get_all_songs():
    d = {}
    d['pop'] = songs_list('pop-songs')
    d['rock'] = songs_list('rock-songs')
    d['rap'] = songs_list('r-b-hip-hop-songs')
    d['dance'] = songs_list('dance-electronic-songs')
    d['country'] = songs_list('country-songs')
    d['latin'] = songs_list('latin-songs')
    return d







