try:
    age = int(input("age: "))
except ValueError as ex:
    print("you didn't enter a vaild age.")
    print(ex)
    print(type(ex))
else:
    print("No exception were thrown")
print("Execution continous")
