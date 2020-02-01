numbers = [1, 2, 3]
# Should be equal to the number of iteams we have in the list
first, second, third = numbers
# Above and below both are same.
first = numbers[0]
second = numbers[1]
third = numbers[2]

numbers = [1, 2, 3, 4, 5, 6]

# iteams and everthing will be stored in a separate list called other.
first, second, *others = numbers
print(first)
print(second)
print(others)

first, *others, last = numbers  # you can get last value using last
print(first, last)
print(others)
