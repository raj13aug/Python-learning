
# Try block if any of these statements thrown an exception that matches one of the except clauses and other except clauses are ignored.

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except (ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exception were thrown")
