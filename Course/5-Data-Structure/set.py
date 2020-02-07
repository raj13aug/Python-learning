# Set is collection with no duplicate 
#unordered collection --> Which means in set are not in sequence so we cannot access them using index.( print(first[0]))

numbers = [1, 2, 1, 4, 5, 1]    # if you want to remove the duplicate items you convert this to a "set".
uniques = set(numbers)
print(uniques)    # only have unique  items so 1 is not repeated.

# We can add new items to set or remove an existing one 

second = {1, 4}
second.add(7)
second.remove(1)
print(len(second))
print(second)

# we get union of two variable, using the vertical bar , it inculde all items. 
print(uniques | second)
print(uniques & second) # It display only same value 
print(uniques - second) # different between two items 
print(uniques ^ second) # Items will present first or second but not both

if 4 in second:
    print("yes")
