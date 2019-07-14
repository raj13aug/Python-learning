high_income = True
good_credit = True
student = True
#And operator:

if high_income and good_credit:
    print("eligible")
else:
    print("Not eligible")

# Or operator:


if high_income or good_credit:
    print("eligible")
else:
    print("Not eligible")


# NOT operator:


if not student:
    print("eligible")
else:
    print("Not NOT eligible")

# combined evluation

if (high_income or good_credit) and not student:
    print("combined")
else:
    print("not combined")
