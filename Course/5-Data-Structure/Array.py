# if you facing any performance problem then you can move from list to array

from array import array

numbers = array("i", [1, 2, 3])
print(type(numbers))
print(numbers)
print(numbers[0])
x = numbers.pop()
print(x)

# we cannot assign the float value to array number beacuse We specified the intger value

numbers[0] = 1.0
