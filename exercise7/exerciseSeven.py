"""Ejercicio 7
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
minutes = int(input("Ingrese una cantidad de minutos: "))
hours = int(minutes/60)
minutes = minutes - hours*60
print("Equivale a: " + str(hours) + " horas con " + str(minutes) + " minutos")