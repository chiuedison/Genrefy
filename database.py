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
    #cur.execute('DROP TABLE IF EXISTS Categories')
    #cur.execute('DROP TABLE IF EXISTS Lengths')
    #cur.execute('DROP TABLE IF EXISTS Lyrics')
    #cur.execute('DROP TABLE IF EXISTS Num_Lyrics')
    cur.execute('CREATE TABLE IF NOT EXISTS Lyrics (Title TEXT PRIMARY KEY, lyrics TEXT)')
    cur.execute("CREATE TABLE IF NOT EXISTS Categories (title TEXT PRIMARY KEY, artist TEXT, category TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Lengths (title TEXT PRIMARY KEY, artist TEXT, length TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Num_Lyrics (title TEXT PRIMARY KEY, artist TEXT, category TEXT, lyrics INTEGER)")
    print('database created')
    conn.commit()


def insert_song_categories(cur, conn, songs, data_count):
    cur.execute('SELECT COUNT(*) from Categories')
    table_rows = cur.fetchone()[0]
    if table_rows == 109:
        return data_count
    for i in songs:
        data_count += cur.execute("INSERT OR IGNORE INTO Categories (title, artist, category) VALUES (?,?,?)", (i[0], i[1], i[2])).rowcount

        if data_count == 25:
            break
    conn.commit()
    return data_count


def insert_song_lengths(cur, conn, songs, data_count):
    cur.execute('SELECT COUNT(*) from Lengths')
    table_rows = cur.fetchone()[0]
    if table_rows == 109:
        return data_count
    for i in songs:
        data_count += cur.execute("INSERT OR IGNORE INTO Lengths (title, artist, length) VALUES (?,?,?)", (i[0], i[1], i[3])).rowcount
        '''
        if data_count == 25:
            break'''
    conn.commit()
    return data_count


    

def insert_song_num_lyrics(cur, conn, songs, data_count):
    cur.execute('SELECT COUNT(*) from Num_Lyrics')
    table_rows = cur.fetchone()[0]
    if table_rows == 109:
        return data_count
    for i in songs:
        data_count += cur.execute("INSERT OR IGNORE INTO Num_Lyrics (title, artist, category, lyrics) VALUES (?,?, ?, ?)", (i[0], i[1], i[2], i[3])).rowcount
        '''        
        if data_count == 25:
            break'''
    conn.commit()
    return data_count


def insert_lyrics(cur, conn, songs, data_count):
    cur.execute('SELECT COUNT(*) from Lyrics')
    table_rows = cur.fetchone()[0]
    if table_rows == 109:
        return data_count
    for i in songs:
        data_count += cur.execute("INSERT OR IGNORE INTO Lyrics (title, lyrics) VALUES (?,?)", (i[0], i[1])).rowcount
        '''
        if data_count == 25:
            break'''
    conn.commit()
    return data_count