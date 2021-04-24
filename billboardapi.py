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
    cur.execute("CREATE TABLE IF NOT EXISTS Billboard (name TEXT PRIMARY KEY, length TEXT")
    conn.commit()

def get_top_songs():
    chart = billboard.ChartData('hot-100')[:25]


def main():
    cur, conn = setUpDatabase('billboard.db')
    create_bb_table(cur, conn)