#Logical Operator

#AND --> Both condition is true then result will be true.
#OR --> Aleast one of condition is true.
#NOT --> basically inverses condition.#AND

high_income = False
good_credit = True
student = False
if high_income and good_credit:
    print("Eligible")
else:
    print("not Eligible")


student = False
if not False:
    print("Eligible")
else:
    print("not Eligible")


if (high_income or  good_credit) and not student:
    print("Eligible")
else:
    print("not Eligible")

