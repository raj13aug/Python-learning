# raise  a value error exception, in partenthesis, we can specify  an error message

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(0)
except ValueError as error:
    print(error)
