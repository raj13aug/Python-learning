letters = ["a", "b", "c"]
# We use the append method to add something at the end of this list
letters.append("a")
print(letters)
# you want to add specific position you should use the insert methond
letters.insert(0, "3")
print(letters)


# Remove
# Pop method removing the end of list
letters.pop()
print(letters)
# use index also
letters.pop(0)
print(letters)
# Remove method removing charater in first
letters.remove("b")
print(letters)

# Delete the range of iteams
del letters[0:1]
print(letters)

# different between pop and del methods
# The pop method will remove only one item by index
# Delete method we remove range of items

# clear all object in list
letters.clear()
print(letters)

