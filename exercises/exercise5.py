"""
Exercise 5:
Write a program that converts a given value in Fahrenheit to Celsius.
Remember that the formula for conversion is:
C = (F - 32) * 5 / 9
"""
fahrenheit = float(input("Type Fahrenheit temperature: "))

celsius = (fahrenheit-32)*5/9

print("Given temperature in Celsius is: %x" % celsius)