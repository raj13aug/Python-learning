numbers = [3, 2, 3, 4, 5, 5]
# new number added into last
numbers.append(20)
print(numbers)
#if you want to add number in begin
numbers.insert(0, 0)
print(numbers)
#if you want to remove number
numbers.remove(0)
print(numbers)
#if you want to clear the all number in list
#numbers.clear()
print(numbers)
# if you want to remove from last
numbers.pop()
print(numbers)

# in-operator, it generator boolean value
print( 2 in numbers)

# if you want to count the number for duplicate list which twice or thice times
print(numbers.count(5))

# if you want to ascending order of list.
numbers.sort()
print(numbers)

# if you want to desascending order of list
numbers.reverse()
print(numbers)

# if you want to copy the one list to another list
number2 = numbers.copy()
numbers.append(8)
print(numbers)
print(number2)


