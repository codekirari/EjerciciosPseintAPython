# 1. Secuencias Simples
# a)Saludo personalizado: Pide el nombre del usuario y escribe "¡Hola, [nombre]!".

nombre = input("Ingresa tu nombre por favor: ")
print("Hola, ", nombre, "!")

# b)Suma de dos números: Pide dos números y muestra el resultado de sumarlos.

num1 = float(input("Elija el primer número: "))
num2 = float(input("Elija el segundo número: "))
suma = num1 + num2
print("La suma de ambos números es: ", suma)

# c)Calculadora de área de un círculo: Pide el radio y calcula el área

radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * (radio ** 2)
print("El área del círculo es: ", area) 



#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


# 2. Condiciones (si-entonces)
# a)Mayor de edad: Pide la edad del usuario y dice si es mayor o menor de 18 años.

edad_usu = int(input("Ingresa tu edad: "))
if edad_usu >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")


# b)Número positivo/negativo/cero: Pide un número y clasificarlo.

clasificar_n = float(input("Ingrese un número para clasificarlo como positivo/negativo/cero: "))
if clasificar_n > 0:
    print("El número es positivo")
elif clasificar_n < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# c)Aprobado o reprobado: Pide una nota (0-10) y muestra "Aprobado" si es >=6.

nota = float(input("Ingresa tu nota (0-10): "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Reprobado.")


# d)Día de la semana: Pide un número del 1 al 7 y muestra el día correspondiente.
dia = int(input("Ingresa un número del 1 al 7: "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido (debe ser del 1 al 7).")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


# 3. Ciclos (mientras o repetir)
# a)Contador del 1 al 10: Imprime los números del 1 al 10 usando un ciclo.

i = 0
while i <= 10:
    print(i)
    i = i + 1

# b)Suma hasta 'n': Pide un número n y suma todos los números desde 1 hasta n.

n = int(input("Ingresa un número n: "))
suma = 0
i = 1
while i <= n:
    suma = suma + i
    i = i + 1
print("La suma de 1 hasta", n, "es:", suma)

# c)Adivina el número: El usuario debe adivinar un número fijo (ej: 5). El programa dice 
# "mayor" o "menor" hasta que acierte.

num_secreto = 5
adivina = int(input("Adivina el número (entre 1 y 10): "))
while adivina != num_secreto:
    if adivina < num_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    adivina = int(input("Intenta de nuevo: "))
print("¡Correcto! Adivinaste, el número era: ", num_secreto)


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


# 4. Integradores 
# a)Factorial de un número: Calcula el factorial de un número ingresado.

n = int(input("Ingresa un número para calcular su factorial: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("El factorial de", n, "es:", fact)

# b)Tabla de multiplicar: Pide un número y muestra su tabla de multiplicar del 1 al 10.

num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1

# c)Promedio de notas: Pide 3 notas y calcula el promedio. Luego, dice si está aprobado 
# (>=60) o no.

n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))
promedio = (n1 + n2 + n3) / 3
print("El promedio es:", promedio)
if promedio >= 60:
    print("Aprobado.")
else:
    print("Reprobado.")

# d)Contador de pares/impares: Pide 5 números y cuenta cuántos son pares e impares.

pares = 0
impares = 0
i = 1
while i <= 5:
    num = int(input("Ingresa un número para saber cuántos son pares e impares: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    i = i + 1
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)

# e)Simulador de cajero básico:
# I. Saldo inicial: $1000.

saldo = 1000
print("Tu saldo actual es: $", saldo)
accion = input("¿Deseas 'retirar' o 'depositar'? ").lower()

if accion == "retirar":
    monto = float(input("¿Cuánto deseas retirar? "))
    if monto <= saldo:
        saldo = saldo - monto
        print("Retiro exitoso. Tu nuevo saldo es: $", saldo)
    else:
        print("Fondos insuficientes.")
elif accion == "depositar":
    # II. Pide al usuario si quiere "retirar" o "depositar".
    monto = float(input("¿Cuánto deseas depositar? "))
    saldo = saldo + monto
    # III. Actualiza el saldo y muéstrelo
    print("Depósito exitoso. Tu nuevo saldo es: $", saldo)
else:
    print("Opción no válida.")