"""Ejercicio 8
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones."""
comisiones = 0.0
sueldoBase = float(input("Ingrese sueldo base: "))
ventasDelMes = [0,0,0]
i = 0
while i < 3:
    ventasDelMes[i] = float(input("Ingrese una venta: "))
    i = i + 1
i = 0
while i <3:
    comisiones += ventasDelMes[i]*0.1
    i = i + 1
print("Total por comisiones: " + str(comisiones))
print("Total del mes: " + str(comisiones + sueldoBase))