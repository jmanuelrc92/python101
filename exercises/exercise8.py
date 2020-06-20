"""
Exercise 8
A seller receives a base salary plus an extra 10% commission on their sales,
the seller wants to know how much money he will get for commissions
for the three sales you make in the month and the total you will receive in the month
taking into account your base salary and commissions.
"""

comisions = 0.0
baseSalary = float(input("Enter base salary: "))
monthSales = [0,0,0]
i = 0
while i < 3:
    monthSales[i] = float(input("Enter a sale amount: "))
    comisions += monthSales[i]*0.1
    i += 1
print("Total comisions: " + str(comisions))
print("Total of the month: " + str(comisions + baseSalary))