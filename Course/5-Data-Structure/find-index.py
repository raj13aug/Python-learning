# find the index number of a letter
letter = ["a", "b", "c"]
print(letter.index("a"))
# if value is doesn't exist, u may get value error
# print(letter.index("d"))


# if don't get error message, if have to use "in" operator

if "d" in letter:
    print(letter.index(d))

# count is number of occurrences of the given item in this list.

letter1 = [1, 3, 5, 5]
print(letter1.count(5))

letter2 = [1, "s", 5, "s"]
print(letter2.count("s"))
