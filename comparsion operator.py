temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

value = input("Please enter your name")
if len(value) <= 3:
    print("name must be at least 3 characters")
elif len(value) >= 50:
    print("name can be a maximum of 50 character")
else:
    print("name looks good!")