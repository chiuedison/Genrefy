import unittest
import json
import os
import sqlite3
import requests

import billboard

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_bb_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS Billboard')
    #cur.execute("CREATE TABLE IF NOT EXISTS Billboard (name TEXT PRIMARY KEY, length TEXT)")
    print('database created')
    conn.commit()

def get_top_songs():
    chart = billboard.ChartData('hot-100')[:25]
    l = []
    for entry in chart:
        t = (entry.title, entry.artist)
        l.append(t)
    return l

def pop_songs():
    chart = billboard.ChartData('pop-songs')[:10]
    l = []
    for entry in chart:
        t = (entry.title, entry.artist)
        l.append(t)
    print(l)


def insert_songs(cur, conn, songs):
    length = '3:00'
    for i in songs:
        cur.execute("INSERT INTO Billboard (name, length) VALUES (?,?)", (i[0], length))
    conn.commit()
def main():
    cur, conn = setUpDatabase('billboard.db')
    create_bb_table(cur, conn)
    pop_songs()
    #insert_songs(cur, conn, get_top_songs())

main()