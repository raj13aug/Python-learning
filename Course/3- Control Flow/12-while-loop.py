number = 100
while number > 0:
    print(number)
    number // 2

# while loop that continues execution until we press control D.
command = ""
while command != "quit" and command != "QUIT":
command = input(">")
print("ECHO", command)

# it convert lower case then compare it.
command = ""
while command.lower() != "quit":
command = input(">")
print("ECHO", command)
