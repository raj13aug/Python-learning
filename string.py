
#
print("python for 'beginner'")
#
print('python /for "beginner"')

#multi line string
course = '''

Hi John,

Here is our first email to you.

Thank you,
The support team

'''

print(course)

#index

store = 'Nataraj'
print(store[1])
print(store[-1])
# character start from 0 to 3. but last character exlude.
print(store[0:3])
# character start from 0 to end
print(store[0:])
# character start from 1 to end. but first character exlude.
print(store[1:])
# Even if you don't enter the start value but python consider as 0 starting value.
print(store[:3])

#copy the content from one variable to another variable.

values = store[:]
print(values)
# Note: only exculde last value which you defined below.
print(values[1:-1])