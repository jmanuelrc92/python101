"""
Exercise 2:
Calculate the perimeter and area of ​​a rectangle given its base and height.
"""
base = float(input("Type rectangle's base: "))
height = float(input("Type rectangle's height: "))

perimeter = 2*base + 2*height
area = base*height

print("Rectangle's perimeter is: " + str(perimeter))
print("Rectangle's area is: " + str(area)+ " u^2")