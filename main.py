import unittest

from database import *
from web import *
from lyrics import *
from calculations import *
from plot import *


def main():
    print('begin')
    cur, conn = setUpDatabase('billboard.db')
    create_bb_tables(cur, conn)
    
    songs = unique_songs(get_data(get_all_songs()))
    data_count = 0
    data_count = insert_song_categories(cur, conn, songs, data_count)
    if data_count == 25:
        return
    data_count = insert_song_lengths(cur, conn, songs, data_count)
    '''
    if data_count == 25:
        return'''
    num_lyrics, lyrics = web_songs(songs)
    data_count = insert_song_num_lyrics(cur, conn, num_lyrics, data_count)
    '''
    if data_count == 25:
        return'''
    data_count = insert_lyrics(cur, conn, lyrics, data_count)
    '''
    if data_count == 25:
        return'''

    write_avg_ratio_of_category(cur, conn, 'Latin')

    plot_lengths(cur, conn)
    plot_lyrics(cur, conn)
    plot_ratios(cur, conn)
    print('end')


main()