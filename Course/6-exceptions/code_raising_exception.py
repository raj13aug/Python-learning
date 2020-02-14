# raise  a value error exception, in partenthesis, we can specify  an error message
from timeit import timeit

code = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(0)
except ValueError as error:
    pass

"""

code1 = """

def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass

"""

print("second code", timeit(code1, number=10))
print("frist code", timeit(code, number=10))
