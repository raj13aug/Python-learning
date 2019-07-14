course = "python programming for beginner"
# Using len function count the number of letter in string
print(len(course))

#using dot function convert the letter to capital character

print(course.upper())
print(course.lower())
print(course.find('y'))
# if we are try to find the  captial letter even doesn't existed in variable as showing as negetive no
print(course.find('Y'))
# you can pass the hole word as well
print(course.find('beginner'))
# Now we can replace the word from beginner to absolute beginner
print(course.replace('beginner','absolute beginner'))
# It's case sensitive
print (course.replace('Beginner','absolute beginner'))
# you can replace with character
print (course.replace('p','j'))
#boolean expression
print('python' in course)
# different operator(in) and characters in our string(find method)
# find method return as index value
# in method return as boolean value.





