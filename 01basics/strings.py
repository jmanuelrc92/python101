# Strings values
"""
String concatenation
Output in both cases:
"JohnDoe"
"John Doe"
"""
print("String concatenation")
print("John""Doe")
print("John" + " " + "Doe")

print("_____________________________________________")

"""
String formating
Use % operator to replace a token %s with a atring variable
Use the %x for integer values.

Output:
"Hello John Doe"
"I see you in 3 days"
"""
fullName = "John Doe"
numberOfDays = 3
print("String formating")
print("Hello %s" % fullName)
print("I see you in %x days" % numberOfDays)

print("_____________________________________________")

"""
String format, only Python 3, replaces the brackets with the values of the variables passed in the format function, in that order
Output:
"Hello I'm John, my age is 20"
"""
name = "John"
age = 28
print("String formating, only in Python 3")
print("Hello I'm {}, my age is {}".format(name, age))