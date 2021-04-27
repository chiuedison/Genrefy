import unittest

import plotly

import database
import api
import web
import lyrics


def main():
    cur, conn = setUpDatabase('billboard.db')
    create_bb_tables(cur, conn)
    
    songs = unique_songs(get_data(get_all_songs()))
    data_count = 0
    insert_song_lengths(cur, conn, songs, data_count)
    if data_count == 25:
        return
    lyrics = web_songs(songs)
    insert_song_lyrics(cur, conn, lyrics, data_count)
    if data_count == 25:
        return


main()