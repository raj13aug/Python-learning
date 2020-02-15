has_high_income = True
has_good_credit = True
has_criminal_record = False
# And operator both condition should be true
# OR operator at least any condition should be true
# NOT operator if you give it true boolean value it convert to false.
if has_high_income or has_good_credit:
    print("Eligible for loan using OR operator")

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
