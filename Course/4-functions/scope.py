message = "a"  # Global value for program


def greet(name):
    global message     # bad practice and you should avoid it all times. it overwrite global value.
    message = "b"      # By default message value is treat as local variable.


greet("Nataraj")
print(message)
