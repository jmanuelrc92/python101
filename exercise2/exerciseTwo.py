"""Exercise two
Calculate
Calcular el perímetro y área de un rectángulo dada su base y su altura."""
base = float(input("Ingrese la medida de la base del rectangulo: "))
altura = float(input("Ingrese la medida de la altura del rectangulo: "))
print("El perimetro del rectangulo es: " + str(2*base + 2*altura))
print("El area del rectangulo es: " + str(base*altura)+ " u^2")