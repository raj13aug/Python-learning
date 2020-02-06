items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 13)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# map function works, it takes a lambda function and applies it to every item of this iterable.

prices = list(map(lambda item: item[1], items))
print(prices)

# https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593
