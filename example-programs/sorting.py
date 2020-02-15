numbers = [2, 1, 4, 6, 5]
#Asdenting order
numbers.sort()
print(numbers)
#Desceding order
numbers.sort(reverse=True)
print(numbers)
#cannot change the value
print(sorted(numbers))
print(sorted(numbers, reverse=True))

items = [
    ("product1", 10),
    ("product2", 9),
    ("Product3", 12),
    ]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

