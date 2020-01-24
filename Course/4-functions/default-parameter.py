def increment(number, by=2):
    return number + by


# if don't supply second argument this default value will be used, otherwise the value we specificed used.
print(increment(3))
print(increment(3, 9))

# we cannot add another required parameter here
# def increment(number, by=2,  another):

# All optional should come before the required paramter.
# def increment(number, another, by=2)
