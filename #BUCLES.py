#BUCLES

#--FOR--

#Ejercicio 1: Contador ascendente
#Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número utilizando un ciclo for.

#n = int(input("Ingrese un número entero positivo: "))
#for i in range(1, n + 1):
#    print(i)

#Ejercicio 2: Suma de números naturales
#Solicite un número entero positivo N y calcule la suma de todos los números desde 1 hasta N.

#n = int(input("Ingrese un número entero positivo: "))
#suma = 0
#for i in range(1, n + 1):
#    suma += i
#print(f"La suma es: {suma}")

#Ejercicio 3: Tabla de multiplicar
#Solicite un número entero e imprima su tabla de multiplicar del 1 al 10 utilizando un ciclo for.

#numero = int(input("Ingrese un número entero: "))
#for i in range(1, 11):
#    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 4: Contador de vocales
#Solicite una palabra o frase e indique cuántas vocales contiene utilizando un ciclo for

#texto = input("Ingrese una palabra o frase: ").lower()
#vocales = "aeiouáéíóúü"
#contador = 0
#for letra in texto:
#    if letra in vocales:
#        contador += 1
#print(f"Cantidad de vocales: {contador}")

#Ejercicio 5: Triángulo de asteriscos
#Solicite un número entero positivo y genere un triángulo de asteriscos utilizando un ciclo for.

#n = int(input("Ingrese un número entero positivo: "))
#for i in range(1, n + 1):
#    print("*" * i)

#--WHILE--
#Ejercicio 1: Contador ascendente
#Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número utilizando un ciclo while

#n = int(input("Ingrese un número entero positivo: "))
#i = 1
#while i <= n:
#    print(i)
#    i += 1

#Ejercicio 2: Suma acumulada
#Solicite números al usuario y acumule la suma.
#El programa debe finalizar cuando el usuario ingrese el valor 0.
#Al finalizar, mostrar la suma total.

#suma = 0
#numero = int(input("Ingrese un número (0 para terminar): "))
#while numero != 0:
#    suma += numero
#    numero = int(input("Ingrese un número (0 para terminar): "))
#print(f"Suma total: {suma}")

#Ejercicio 3: Validación de contraseña
#Solicite una contraseña al usuario. 
#Mientras la contraseña ingresada sea diferente de:
#python123
#debe volver a solicitarla.
#Cuando la contraseña sea correcta, mostrar:
#Acceso concedido

#contrasena = input("Ingrese la contraseña: ")
#while contrasena != "python123":
#    contrasena = input("Contraseña incorrecta. Intente nuevamente: ")
#print("Acceso concedido")

#Ejercicio 4: Control de asistencia
#Solicite la cantidad de estudiantes presentes en cada clase.
#El ingreso finalizará cuando el usuario introduzca el valor -1.
#Al finalizar, mostrar:
#Total de asistencias registradas.
#Cantidad de clases ingresadas.
#Promedio de asistencia.

#total = 0
#clases = 0
#asistencia = int(input("Estudiantes presentes (-1 para terminar): "))
#while asistencia != -1:
#    total += asistencia
#    clases += 1
#    asistencia = int(input("Estudiantes presentes (-1 para terminar): "))
#print(f"Total de asistencias: {total}")
#print(f"Cantidad de clases: {clases}")
#if clases > 0:
#    promedio = total / clases
#    print(f"Promedio de asistencia: {promedio}")
#else:
#    print("Promedio de asistencia: no hay clases registradas")

#Ejercicio 5: Caja registradora
#Solicite el precio de los productos comprados.
#El ingreso finalizará cuando el usuario ingrese 0.
#Al finalizar mostrar:
#Cantidad de productos.
#Monto total de la compra.

#cantidad = 0
#total = 0
#precio = float(input("Precio del producto (0 para terminar): "))
#while precio != 0:
#    cantidad += 1
#    total += precio
#    precio = float(input("Precio del producto (0 para terminar): "))
#print(f"Productos comprados: {cantidad}")
#print(f"Total a pagar: {total}")