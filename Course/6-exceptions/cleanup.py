#Throws an exception and file.close() will not execusted.solution is final clause at the end.
#It always execusted whether we have an exception formot. it's perfect place is close files and so on.

try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except (ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exception were thrown")
finally:
    file.close()
