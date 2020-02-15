#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

#https://www.w3schools.com/python/python_lambda.asp `
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 8),

]
print(type(items))
items.sort(key=lambda item:item[1])
print(items)