#Autor: Sebastián Triana

#Estos son 6 ejercicios con estructuras de control

#1. Ejercicio #12: Escribir un programa en python que imprima por pantalla los números del 5 al 15

for i in range(5, 16):
    print(i)

print("--------------------------------")


#2. Ejercicio #14:Escribir un programa en python que imprima 200 veces la palabra “hola”. Nota: en elcódigo fuente que usted escriba debe figurar solamente una vez la palabra “hola”.

for i in range(200):
    print(f"{i + 1}. hola")

print("--------------------------------")


#3. Ejercicio #18: Escribir un programa en python que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla.

numero = int(input("Numero entero porfavor: "))
suma = 0

for i in range(numero + 1, numero + 101):
    suma += i
print(f"Los 100 números siguientes a {numero} sumados da: {suma}")

print("--------------------------------")


#4 Ejercicio #21: Escribir un programa en python que lea dos números del teclado y diga cual es el mayor y cual el menor.

input1 = float(input("Primer número: "))
input2 = float(input("Segundo número: "))

if input1 > input2:
    print(f"Numero mayor: {input1}")
    print(f"Número menor: {input2}")
elif input1 < input2:
    print(f"Número mayor: {input2}")
    print(f"Número menor: {input1}")
else:
    print("Son numeros iguales mi loco.")

print("--------------------------------")

#5 Ejercicio22: Escribir un programa en Python que lea un número entero por el teclado e imprima todos los número impares menores que él.

numero = int(input("Número entero: "))
print("los números impares menores que", numero, "son:")
for i in range(1, numero, 2):
    print(i)

print("--------------------------------")

#6 Ejercicio 26: Escriba un programa que lea tres números enteros positivos, y que calcule e imprima en pantalla el menor y el mayor de todos ellos.

num1 = int(input("Ingrese un número entero positivo: "))
num2 = int(input("Ingrese otro número entero positivo: "))
num3 = int(input("Ingrese un último número entero positivo: "))


if num1 > num2:
    mayor = num1
if num3 > num3:
    mayor = num3

if num1 < num2:
    menor = num1
if num3 < num3:
    menor = num3

print("El número menor es:", menor)
print("El número mayor es:", mayor)