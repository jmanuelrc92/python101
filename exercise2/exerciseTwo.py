"""Exercise two
Calcular el perímetro y área de un rectángulo dada su base y su altura."""
base = float(input("Ingrese la medida de la base del rectangulo: "))
height = float(input("Ingrese la medida de la altura del rectangulo: "))
print("El perimetro del rectangulo es: " + str(2*base + 2*height))
print("El area del rectangulo es: " + str(base*height)+ " u^2")