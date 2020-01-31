letters = ["a", "b", "c", "d"]
# To access individual items in this list.
print(letters[0])
print(letters[-1]) # negative index here.
# we can modify items in the list
letters[0] = "A"
print(letters)
#slice 
print(letter[0:3])
print(letter[:])
print(letter[::])  # It will print everty 2 element of list.

numbers = list(range(20))
print(numbers[::2])  # print all even numbers
print(numbers[::-1]) # it will return all items in reverse order.
