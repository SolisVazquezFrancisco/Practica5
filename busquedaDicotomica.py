import math

numero = [1,2,3,4,5,6,7,8,9]
print("Numero que Buscar")

numeroBuscar = int(input())
posicion = -1
incremento = round(len(numero)/2)
ubicacion = incremento

while posicion == -1:

    if (numeroBuscar == numero[ubicacion]):
        posicion = ubicacion

    elif (numeroBuscar > numero[ubicacion]):
        incremento = math.ceil(incremento/2)
        ubicacion += incremento

    else:
        incremento = math.ceil(incremento/2)
        ubicacion -= incremento

print(posicion+1) 