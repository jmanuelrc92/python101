"""Ejercicio 3
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
import math
cateto1 = float(input("Ingrese medida cateto 1: "))
cateto2 = float(input("Ingrese medida cateto 2: "))
#c^2 = a^2 + b^2
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print("La medida de la hipotenusa es: " + str(hipotenusa))