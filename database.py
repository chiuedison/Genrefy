import unittest
import sqlite3
import json
import os
import requests
from web import *
from billboardapi import *

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def create_bb_tables(cur, conn):
    #cur.execute('DROP TABLE IF EXISTS Lengths')
    #cur.execute('DROP TABLE IF EXISTS Lyrics')
    cur.execute("CREATE TABLE IF NOT EXISTS Lengths (title TEXT PRIMARY KEY, artist TEXT, category TEXT, length TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Lyrics (title TEXT PRIMARY KEY, artist TEXT, category TEXT, lyrics INTEGER)")
    print('database created')
    conn.commit()

def insert_song_lengths(cur, conn, songs, data_count):
    cur.execute('SELECT COUNT(*) from Lengths')
    table_rows = cur.fetchone()[0]
    if table_rows == 106:
        return
    for i in songs:
        data_count += cur.execute("INSERT OR IGNORE INTO Lengths (title, artist, category, length) VALUES (?,?,?,?)", (i[0], i[1], i[2], i[3])).rowcount
        if data_count == 25:
            break
    conn.commit()

    

