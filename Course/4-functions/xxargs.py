# when we use double asterisks here we can pass multiple key value pairs here, or multiple key word arguments to a function.
def save_user(**user):
    print(user)


save_user(id=1, name="vino", age=22)
# output showing as dictionaries function


def save_user(**user):
    print(user["name"])


save_user(id=1, name="vino", age=22)
# We can acess the only variable
