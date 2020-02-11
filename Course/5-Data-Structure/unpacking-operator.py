# unpacking operator, to take out individual values in any operator
# if printing out individual numbers, individual items  in out list

# prefix this variable to the unpacking opertor.
numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
print(values)

# unpack opertor any iterable
values = [*range(5), *"Hello"]
print(values)

# combine list
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# two asterisks for dictories

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
