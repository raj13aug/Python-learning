# With statement, python will automatically call file.close whether we have a final clause or not.

try:
    with open("app.py") as file:
        print("File Opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown")
