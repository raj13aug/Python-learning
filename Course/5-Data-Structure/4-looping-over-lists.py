letters = ["a", "b", "c"]
for letter in letters:
    print(letter)


#
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)

# you will get index value
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0])

# you will get index value and list value
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])

#
for index, letter in enumerate(letters):
    print(index, letter)
# enumerate function returns an enumerate object which is iterable. The enumerate object will return a tuple that looks like this

