import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten cop", "year": 1993}
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_test(data)

data = Path("movies.json").read_test()
movies = json.loads(data)
print(movies)
print(movies)[0]["title"])
