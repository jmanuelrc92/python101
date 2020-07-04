"""
Exercise 7:
Make a program that receives a number of minutes and shows on the screen how many hours and minutes it corresponds.
For example: 1000 minutes is 16 hours and 40 minutes.
"""

totalMinutes = int(input("Enter a number of minutes: "))
hours = int(totalMinutes/60)
minutes = totalMinutes - hours*60
print("{0} minutes are equivalent to {1} hours and {2} minutes.".format(totalMinutes, hours, minutes))