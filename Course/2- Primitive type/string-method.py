course = "Python Programming"
# It doesn't affacted by orginital string.convert to upper letter
print(course.upper())
course_capital = course.upper()  # store in the variable
print(course.lower())  # covert to lowercase.
print(course.title())  # capitalize frist caracter of every word
course = "     Python Programming  "
# it use to trim any white space at the begining or end of a string.
print(course.strip())
print(course.lsstrip())  # left strip
# right strip It will remove white space from the end of a string.
print(course.rsstrip())
# A character or a series of characters, find the index of pro also python case sensitive language.
print(course.find("pro"))
# you will get -1 that means the string was not found.
print(course.find("Pro"))
print(course.replace("P", "j")  # we can replace a character or a sequence of character.

print("r" in course)  # expression checks to see if we have pro in course.
print("swift" not in course)  # not operator

# difference between find and in

# 1.find method returns that index.
# 2.In expression returns a boolean so it's a true or false.
