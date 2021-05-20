"""
Exercise 10
Ask the user two numbers, and show "the distance" between them.

Distance:
The absolute value of the difference between them.
"""

number1 = float(input("Type the first number: "))
number2 = float(input("Type the second number: "))

if (number2 < number1):
    aux = number1
    number1 = number2
    number2 = aux

difference = 0
while number1 < number2:
    difference += 1
    number1 += 1

print("Difference between numbers is: " + str(difference))