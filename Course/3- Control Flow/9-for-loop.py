successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
#break --> break statement stop the process execustion for next loop.
#################################

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
else:
    print("Attempted 3 times and failed")
