# [] - -> Define a list of a sequence of objects.
# we can combine a list of numbers, booleans with string or even a list of lists.
letters = ["a", "b", "c"]
#matrix[[0, 1], [2, 3]]
# using asterisk we can repeat the items in a list also we can use a plus to concatenate multiple lists.
zeros = [0] * 100
print(zeros)
combined = zeros + letters
numbers = list(range(20))  # iterable
print(numbers)
strings = list("hello world")
print(strings)
print(len(strings))  # length of strings

