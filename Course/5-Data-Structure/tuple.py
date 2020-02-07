Tuples --> Immutable sequence

We can use it to contain a sequence of object but we cannot modify this sequence, we cannot modify a new object to it called as tuple.

point = (1, 2)
print(type(point))

point = 1,  # it consider as tuples
point = () it treat as empty tuples.

We can concatenate two tuples

point = (1, 2) + (3, 4)
print(point)

Also use the multiplication operator 

point = (1, 2) * (3, 4)
print(point)

Also convert a list to tuple

point = tuple(iterable)
print(point)

point = tuple(" Hello World")
print(point)

We can acess the 

