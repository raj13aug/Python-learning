values = []
for x in range(5):
    values.append(x * 2)

# [expression for item in items]

# Extactly identical

values = [x * 2 for x in range(5)]
print(values)

# sets --> curly value, in set we just in values,but in dictionaries we have key value pairs
values = {x * 2 for x in range(5)}
print(values)

values = {x: x * 2 for x in range(5)}
print(values)
