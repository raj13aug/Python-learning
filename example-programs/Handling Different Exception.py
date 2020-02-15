try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("you didn't enter a valid age.")
except ZeroDivisionError:
    print("Age is cannot be 0")
else:
    print("No exception were thrown")
print("Execution continues")

###############################

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exception were thrown")
print("Execution continues")