import unittest
import sqlite3
import json
import os
import requests

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_tables(cur, conn):
    '''cur.execute("DROP TABLE IF EXISTS Apple-Listens")
    cur.execute("DROP TABLE IF EXISTS Spotify-Listens")
    cur.execute("DROP TABLE IF EXISTS Apple-Lengths")
    cur.execute("DROP TABLE IF EXISTS Spotify-Lengths")'''

    cur.execute("CREATE TABLE Apple-Lengths (name TEXT PRIMARY KEY length TEXT")
    cur.execute("CREATE TABLE Spotify-Lengths (name TEXT PRIMARY KEY length TEXT")
    cur.execute("CREATE TABLE Apple-Listens (name TEXT PRIMARY KEY listens NUMBER")
    cur.execute("CREATE TABLE Spotify-Listens (name TEXT PRIMARY KEY listens NUMBER")

    conn.commit()
    
def insert_data(cur, conn, data):
    #data should be a dictionary with keys being the table names and values being a list of tuples (name, length/listens)
    for table in data:
        for song in data[table]:            
            if table.find('lengths') != -1:
                cur.execute("INSERT INTO " + table + " (name, length) VALUES (?,?)", (song[0]), song[1]))
            else:
                cur.execute("INSERT INTO " + table + " (name, listens) VALUES (?,?)", (song[0]), song[1]))
    conn.commit()


def main():
    cur, conn = setUpDatabase('music.db')
    create_tables(cur, conn)
