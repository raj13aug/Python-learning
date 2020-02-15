temperature = 35
if temperature > 70:
    print("Tt's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

##########################################

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)

##########################################

message = "eligible" if age >=  18 else "not eligible"
print(message)
