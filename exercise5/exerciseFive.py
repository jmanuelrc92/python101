"""Ejercicio 5
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es:
C = (F-32)*5/9"""
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit-32)*5/9
print("La temperatura en grados Celsius es: " + str(celsius))