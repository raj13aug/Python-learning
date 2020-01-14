for number in range(3):
    print(number)
    print("Attempt", number)
#number is variable
#Range function start from 0 value
    print("Attempt", number + 1)
    print("Attempt", number + 1, (number + 1 ) * ".")

# range value start from 1 value and end to 4 value.
for number in range(1, 4):
    print("Attempt", number, number * ".")

# We also pass a third argument as a step

for number in range(1, 10, 5):
    print("Attempt", number, number * ".")
