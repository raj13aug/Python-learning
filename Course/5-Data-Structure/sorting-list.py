# Asecending order
numbers = [3, 2, 1, 6, 7]
numbers.sort()
print(numbers)

# descending order
numbers = [3, 2, 1, 6, 7]
numbers.sort(reverse=True)
print(numbers)

# addition function called sorted() also iterable, so we can pass any iterable here and it cannot change the orginal list.
numbers = [3, 2, 1, 6, 7]
print(sorted(numbers))
print(numbers)

# Reverse order
numbers = [3, 2, 1, 6, 7]
print(sorted(numbers, reverse=True))
print(numbers)

# items = [
#("product1", 10),
#("product2", 20),
#("product3", 30)

# ]
# items.sort()
# print(items)  # nothing is changed here. because python doesn't know how to sort list

items = [
    ("product1", 50),
    ("product2", 20),
    ("product3", 30)

]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)
