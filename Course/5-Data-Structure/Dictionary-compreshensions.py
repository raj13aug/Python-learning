from sys import getsizeof

values = [x * 2 for x in range(10)]
print(values)
for x in values:
    print(x)
# generator object  are iterable, so unlike list, they don't store all value and memory, they generator new value in each iteration.
values = (x * 2 for x in range(10))
print(values)

# sizeof
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

# generator objects don't store all items in memory also  only acess these items iterate over a genertor object
