iteams = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 13)
]

# Lambda is one line anonymous fuctions that we can pass to other function.

# syntax:

# lambda arguments : expression

iteams.sort(key=lambda iteams: iteams[1])
print(iteams)
