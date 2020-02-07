#Tuples --> Immutable sequence

#We can use it to contain a sequence of object but we cannot modify this sequence, we cannot modify a new object to it called as tuple.

point = (1, 2)
print(type(point))

point = 1,  # it consider as tuples
point = () #it treat as empty tuples.

#We can concatenate two tuples

point = (1, 2) + (3, 4)
print(point)

#Also use the multiplication operator 

point = (1, 2) * 3
print(point)

#Also convert a list to tuple

point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

#We can acess the  individual item using an index
 
point = (1, 3, 10)
print(point[0])

print(point[0:1])

x, y, z = point

if 10 in point:
    print("exists")
