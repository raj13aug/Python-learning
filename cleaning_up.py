try:
    file = open("2d.py")
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    file.close()
#

# In this case doesn't required finally statement
try:
    with open("2d.py") as file:
    age = int(input("Enter your age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("No exceptions were thrown")
