#Autor: Sebastián Triana

#Estos son 6 ejercicios con estructuras de control

#1. Ejercicio #12: Escribir un programa en python que imprima por pantalla los números del 5 al 15

def imprimir_numeros():
    for i in range(5, 16):
        print(i)
    print("--------------------------------")


#2. Ejercicio #14:Escribir un programa en python que imprima 200 veces la palabra “hola”. Nota: en elcódigo fuente que usted escriba debe figurar solamente una vez la palabra “hola”.

def hola():
    for i in range(200):
        print(f"{i + 1}. hola")
    print("--------------------------------")



#3. Ejercicio #18: Escribir un programa en python que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla.

def enteros_siguientes(n):
    suma = 0
    for i in range(n + 1, n + 101):
        suma += i
    print(f"Los 100 números siguientes a {n} sumados dan: {suma}")
    print("--------------------------------")



#4 Ejercicio #21: Escribir un programa en python que lea dos números del teclado y diga cual es el mayor y cual el menor.

def mas_menos(n1, n2):
    if n1 > n2:
        print(f"Número mayor: {n1}")
        print(f"Número menor: {n2}")
    elif n1 < n2:
        print(f"Número mayor: {n2}")
        print(f"Número menor: {n1}")
    else:
        print("Son números iguales mi loco.")
    print("--------------------------------")


#5 Ejercicio22: Escribir un programa en Python que lea un número entero por el teclado e imprima todos los número impares menores que él.

def impares_menores(n):
    print(f"Los números impares menores que {n} son:")
    for i in range(1, n, 2):
        print(i)
    print("--------------------------------")
    


#6 Ejercicio 26: Escriba un programa que lea tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos ellos.

def mayor_menor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else:
        mayor = n3

    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3

    if n1 < 0 or n2 < 0 or n3 < 0:
        print("Por favor ingrese solo números enteros positivos.")

    if n1 == n2 == n3:
        print("Los tres números son iguales.")
    else:
        print(f"Número mayor: {mayor}")
        print(f"Número menor: {menor}")
    print("--------------------------------")

#7 Ejercicio 28: Implemente una sentencia switch que escriba un mensaje en cada caso. Inclúyala en bucle de prueba for. Utilice también un break tras cada caso y pruébelo. Elimine el break y vea qué ocurre.

def switch():
    for i in range(1, 3):
        match i:
            case 1:
                print("Primer caso")
            case 2:
                print("Segundo caso")
            case _:
                print("Este es por defecto")

#8 Ejercicio #27: Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius mostrándola. El programa finalizará cuando lea un valor de temperatura igual a 999. La conversión de grados Farenheit (F) a Celsius (C) está dada por C = 5/9(F − 32).

def fahrenheit_a_celsius():
    while True: # el while esta para que podamos salir del programa, en otras palabras para que el break tenga sentido
        f = float(input("Ingrese temperatura en Fahrenheit (999 para salir): "))
        match f:
            case 999:
                    print("Programa terminado.")
                    break #(aquí la razon del bucle ese)
            case _:
                    c = (5 / 9) * (f - 32)
                    print(f"{f}°F equivalen a {c:.2f}°C")
    print("--------------------------------")


#9 Ejercicio 30: Escriba un programa que use dos bucles for anidados y el operador de módulo (%) para detectar e imprimir números primos.

def primos_hasta_n():
    n = int(input("Ingrese hasta qué número quiere buscar primos: "))

    print(f"Números primos hasta {n}:")
    for num in range(2, n + 1):  
        es_primo = True
        for i in range(2, num):  
            if num % i == 0:
                es_primo = False
                break  
        if es_primo:
            print(num)
    print("--------------------------------")

#10 Ejercicio 19: Escribir un programa en Java que convierta de euros a dólares. Recibirá un número decimal correspondiente a la cantidad en euros y contestará con la cantidad correspondiente en dolares.

def euros_a_dolares():
    tasa = 1.08 
    euros = float(input("Ingrese cantidad en euros: "))
    dolares = euros * tasa
    print(f"{euros}€ equivalen a {dolares:.2f}$")
    print("--------------------------------")


def main():
    print("Ejercicio 12 ")
    imprimir_numeros()

    print("Ejercicio 14 ")
    hola()

    print("Ejercicio 18 ")
    num = int(input("Ingrese un número entero: "))
    enteros_siguientes(num)

    print("Ejercicio 21 ")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    mas_menos(n1, n2)

    print("Ejercicio 22 ")
    num = int(input("Número entero: "))
    impares_menores(num)

    print("Ejercicio 26 ")
    n1 = int(input("Ingrese un número entero positivo: "))
    n2 = int(input("Ingrese otro número entero positivo: "))
    n3 = int(input("Ingrese un último número entero positivo: "))
    mayor_menor(n1, n2, n3)

    print("Ejercicio 27 ")
    fahrenheit_a_celsius()

    print("Ejercicio 28 ")
    switch()
    
    print("Ejercicio 30 ")
    primos_hasta_n()

    print("Ejercicio 19 ")
    euros_a_dolares()

main()
