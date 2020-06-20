"""
Exercise 10
A student wants to know what their final grade will be in the matter of Algorithms.
That grade is made up of the following percentages:
55% of the average of their three partial grades.
30% of the final exam grade.
15% of the final work grade.
"""

i = 0
partialGrade = 0
while i < 3:
    inputMessage = "Enter partial grade " + str(i + 1) + ": "
    grade = float(input(inputMessage))
    if grade > 0:
        grade = grade/3
    partialGrade += grade
    i += 1
finalTestGrade = float(input("Enter final test grade: "))
finalProjectGrade = float(input("Enter final project grade: "))

finalGrade = (partialGrade*0.55) + (finalProjectGrade*0.3) + (finalProjectGrade*0.15)
print("Final grade is: " + str(finalGrade))