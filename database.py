import sqlite3

import csv


conn = sqlite3.connect("ipod_db")
conn.execute("drop table ipod_tracks")
conn.execute(
    """create table ipod_tracks (artist varchar(500), album varchar(500),  title varchar(500),dir varchar(500))"""
)
with open("mp3_data.csv", "r") as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter

    to_db = [(i["artist"], i["album"], i["title"], i["dir"]) for i in dr]

conn.executemany(
    "INSERT INTO ipod_tracks (artist, album, title, dir) VALUES (?, ?, ?, ?);", to_db
)
conn.commit()
conn.close()
