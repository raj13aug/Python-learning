chars = ['A', 'B', 'c']
fruit = ('Apple', 'banana', 'cherry')
dict = {'name': 'Nataraj', 'ref': 'python', 'sys': 'win'}

# items method -->  to display key and value.

for key, value in dict.items():
    print( key, '=', value)
# enumerate to display index number

for item in enumerate(chars):
    print(item)

# zip method element value combined together

for item in zip(chars, fruit):
    print(item, end = '')

for ran in range(1,6,2):
    print(ran)


