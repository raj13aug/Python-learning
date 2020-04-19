
# All is built in function

# int(x)
# float(x)
# bool(x)
# str(x)


# print(type(x)) check the type of value. whether string or float

# Boolean
# "" -> emtmy string considered as falsey
# 0 is also falsey,
# None

x = input("x: ")        # Input value always coming from string value, so we have to convert the integer value.
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

print(bool(0))  # -> False
print(bool(1))  # -> True
print(bool(-1))  # -> True
print(bool(5))  # -> True
print(bool(""))  # -> False
print(bool("False"))  # -> True
