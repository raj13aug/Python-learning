# Filter like iterate over our list of items, for each item we get the prize, if it matches our criteria.

items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 13)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
