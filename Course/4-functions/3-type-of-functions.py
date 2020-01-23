# 1 - perform a task -> functions that carry out the task.
# 2 - Return a value -> return statement to return a value from this function.



def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("mosh")
print(message)

----------------------------------------------------------------------------
# None value --> #So Python all functions by default return a  none value.


def get(value):
    print(f"{value}")


print(get("one"))

-------------------------------------------------------------------------------
# You can define any return value 


def get1(value1):
    print(f"{value1}")
    return "...."


print(get1("one"))
