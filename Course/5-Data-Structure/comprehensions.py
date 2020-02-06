items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 13)
]

# comprehensions is cleaner and more performance
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

filtered = list(filter(lamnda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
