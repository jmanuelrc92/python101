"""
Exercise 3:
Given the legs of a right triangle, calculate its hypotenuse.
"""

import math
leg1 = float(input("Type leg 1: "))
leg2 = float(input("Type leg 2: "))
#c^2 = a^2 + b^2
hypotenuse = math.sqrt((leg1**2) + (leg2**2))

print("Hypotenuse for given triangle's legs is: %x" % hypotenuse)