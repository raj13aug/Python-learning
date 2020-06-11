# Empty list
prices = []

# objects (in case, sine float)

temps = [ 0.2, 5, 0.8, 0.9 ]
print(temps)

# list of string object

words = ['hello', 'world']

#mixed object 

car_details = ['toyota', 2.2, 'Rava', 6088]

odd_and_ends = [ [1,2,3], ['a', 'b', 'c'], ['one', 'two', 'three'] ]

#######################################


found = []
found.append("a")
print(found)
print(len(found))



# The object in and not input,
# Append work as "u" doesn't currently exist within the found list 

if 'u' not in found:
  found.append("u")
  print(found)

###################################

# Remove object from list

nums = [1, 2, 3, 4]
# This is *not* an index value, its value to remove
print(nums.remove(3))
print(nums)

# pop remove item in the last

nums.pop()
print(nums)


# This is an index value. zero corresponds to the first object in the list.list

nums.pop(0)
print(nums)

############################################

#extending a list with object also appending mutiple value into list of object 
nums.extend([3,4,5])
print(nums)

################################################

#insert    
# The index of the object to insert 
nums.insert(0, 1)
print(nums)


#########################
#copying value from one list to another list

numbers = nums.copy()
print(numbers)

print(nums.append('a'))
print(nums)
print(numbers)
print(numbers[])

#####################################
