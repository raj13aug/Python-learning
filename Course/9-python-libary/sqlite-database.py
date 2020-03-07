import sqlite3
import json
from pathlib import Path

movies = json.load(Path("movies.json").read_test())

with sqlite3.connect("db.sqlite3") as conn:
    command = "insert into movies values(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))

    conn.commit()         # Only require write of table


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    movies = cursor.fetchall()
    print(movies)
