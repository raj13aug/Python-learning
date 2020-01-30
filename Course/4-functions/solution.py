def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    else:
        return "Buzz"


print(fizz_buzz(6))


def fizz_buzz1(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "buzz"
    return input


print(fizz_buzz1(12))
