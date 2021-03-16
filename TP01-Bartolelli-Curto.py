# T.P. 01 - VISIÓN POR COMPUTADORA
import random


def adivinar(cantidad_intentos):
    numero_aleatorio = random.randint(0, 100)
    contador_intentos = 0

    while contador_intentos < cantidad_intentos:
        numero_elegido = int(input("Ingrese un número entre 0 y 100: "))
        contador_intentos += 1
        if numero_elegido == numero_aleatorio:
            print("¡Felicidades! Adivinaste el número ", str(numero_aleatorio), " en ", str(contador_intentos),
                  " intentos ")
            break
        elif numero_elegido < numero_aleatorio:
            print("El numero a adivinar es MAYOR que el ingresado")
        else:
            print("El numero a adivinar es MENOR que el ingresado")
    else:
        print("No adivinaste el número....Era el ", str(numero_aleatorio))

cantidad_intentos = int(input("Ingrese la cantidad de intentos que desea tener: "))
adivinar(cantidad_intentos)