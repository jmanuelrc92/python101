"""Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final."""

i = 0
partialGrade = 0
while i < 3:
    inputMessage = "Ingrese calificacion parcial " + str(i + 1) + ": "
    grade = float(input(inputMessage))
    if grade > 0:
        grade = grade/3
    partialGrade += grade
    i += 1
finalTestGrade = float(input("Ingrese calificacion de examen final: "))
finalProjectGrade = float(input("Ingrese calificacion de proyecto final: "))

finalGrade = (partialGrade*0.55) + (finalProjectGrade*0.3) + (finalProjectGrade*0.15)
print("La calificacion final es: " + str(finalGrade))