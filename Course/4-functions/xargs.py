def multiply(*numbers):  # * to indicate that this  is a collection  of arguments
    total = 1
    for number in numbers:
        print(number)
        total *= number
    return total


multiply(2, 3, 4, 5)


def multiply(*numbers):  # *
    print(numbers)


multiply(2, 3, 4, 5)
